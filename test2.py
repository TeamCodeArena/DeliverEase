#TODO create a table order where request for the order and assignees are saved
from flask import Flask, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.sql import func

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
    app.secret_key = "jlsjfl"
    db = SQLAlchemy(app)

    return app, db
app, db = create_app()



class Seller(db.Model, UserMixin):
    __tablename__ = 'seller'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phoneNo = db.Column(db.String(100))
    address = db.Column(db.String(100))
    experience = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.name} {self.id} {self.email} {self.phoneNo} {self.email} {self.address}"


class Buyer(db.Model):
    __tablename__ = 'buyer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phoneNo = db.Column(db.String(100))
    address = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.name} {self.id} {self.email} {self.phoneNo} {self.email} {self.address}"



class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    pickup_address = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    product_type = db.Column(db.String(100))
    pickup_time = db.Column(db.String(100))
    delivery_address = db.Column(db.String(1000))
    delivery_time = db.Column(db.String(100))
    delivery_pincode = db.Column(db.String(100))
    pickup_pincode = db.Column(db.String(100))
    created_by = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    order_tag = db.Column(db.Integer, unique=True)
    assigned_to = db.Column(db.Integer, db.ForeignKey('seller.id'), default=0)
    status = db.Column(db.String(100), default='Pending')
    rating = db.Column(db.Integer, default='NIL')
    def __repr__(self) -> str:
        return f"Job ID: {self.id} Job Status: {self.status} Item Type: {self.product_type} Pickup Address: {self.pickup_address} Job Created: {self.date} Job OrderTag: {self.order_tag} Pickup Time:{self.pickup_time} Delivery Address: {self.delivery_address} Delivery Time: {self.delivery_time} Delivery Pincode: {self.delivery_pincode} Pickup Pincode: {self.pickup_pincode} Created By: {self.created_by} Assigned_To: {self.assigned_to}"

    # buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    # assigned_to = db.Column(db.Integer, db.ForeignKey('seller.id'), default=0)
    # unique_identifier = db.Column(db.Integer, unique=True)
# def assign_job(order_tag, buyer_id, seller_email):
#
#     seller = Seller.query.filter_by(email=seller_email).first() ## check if the seller is in the database
#     print(seller)
#     seller_id = seller.id
#     print(seller_id)
#     buyer_job = Job.query.filter_by(created_by=buyer_id, assigned_to=0).filter_by(
#         order_tag=order_tag).first() ## checks if the job is available
#     print(buyer_job)
#     if buyer_job:
#         request_made = Order.query.filter_by(buyer_id=buyer_id, seller_id=seller_id).filter_by(
#             order_tag=order_tag, request_status='Pending').first()
#         if request_made:
#             print('request', request_made)
#             request_made.request_status = 'Accepted'
#             db.session.commit()
#             buyer_job.assigned_to = seller_id  ## assigns if the job is available
#             db.session.commit()
#
#             print('Job assigned')

def assign_job(order_tag, seller_id, buyer_email):

    buyer = Buyer.query.filter_by(email=buyer_email).first()
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)
    buyer_job = Job.query.filter_by(created_by=buyer_id, assigned_to=0).filter_by(
        order_tag=order_tag).first() ##checks if the job is available
    # print('Job', buyer_job)
    if buyer_job:
        buyer_job.assigned_to = seller_id
        db.session.commit()
        buyer_job.status = "In Progress"
        db.session.commit()
        print('Job Assigned')
    else:
        print('Job already assigned to someone')

def cancel_job(order_tag, seller_id, buyer_email):

    buyer = Buyer.query.filter_by(email=buyer_email).first()
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)
    buyer_job = Job.query.filter_by(created_by=buyer_id, assigned_to=seller_id).filter_by(
        order_tag=order_tag).first() ##checks if the job is available
    # print('Job', buyer_job)
    if buyer_job:
        buyer_job.assigned_to = 0
        db.session.commit()
        buyer_job.status = "Cancelled"
        db.session.commit()
        print('Job Cancelled Success')
    else:
        print('Job not  assigned to you')

def display_jobs():
    number_of_jobs = Job.query.count()
    if number_of_jobs < 5:
        jobs = Job.query.filter_by(assigned_to=0).order_by(func.random()).limit(number_of_jobs).all()
    else:
        jobs = Job.query.filter_by(assigned_to=0).order_by(func.random()).limit(5).all()
    # Print the job details
    for job in jobs:
        print(job)

def order_completed(order_tag, seller_id, buyer_email, rating):
    buyer = Buyer.query.filter_by(email=buyer_email).first()
    print('Buyer', buyer)
    buyer_id = buyer.id
    print('Buyer ID', buyer_id)
    buyer_job = Job.query.filter_by(created_by=buyer_id, assigned_to=seller_id).filter_by(
        order_tag=order_tag, status='In Progress').first()
    if buyer_job:
        print(buyer_job)
        buyer_job.status = 'Completed'
        db.session.commit()
        buyer_job.rating = rating
        db.session.commit()
        print('Order Completed Successfully')
        print(buyer_job)
    else:
        print('Error')

def get_reviews(seller_id):
    seller_reviews = Job.query.filter_by(assigned_to=seller_id, status='Completed').all()
    for review in seller_reviews:
        print(review.rating)


with app.app_context():
    db.create_all()
    # new_seller = Seller(experience='None', email='aryan@seller', name='username', password='password123', phoneNo='1234567890', address='123 Main St')
    # db.session.add(new_seller)
    # db.session.commit()
    # new_buyer = Buyer(email='aryan@buyer', name='username', password='password123', phoneNo='1234567890', address='123 Main St')
    # db.session.add(new_buyer)
    # db.session.commit()
    #
    # new_job = Job(pickup_pincode='2323432', delivery_pincode='sfhshffh', pickup_address='123 Elm St'
    #               , pickup_time='10:00 AM', delivery_address='456 Oak St'
    #               , delivery_time='1:00 PM', created_by=1, order_tag=1234, product_type='food')
    # db.session.add(new_job)
    # db.session.commit()
    #


    # job_id = 1

    # job = Buyer.query.get(job_id)
    # print(f"The job with id {job_id} is {job}.")
    # for x in range(5):
    job_id = 1
    # job = Job.query.get(job_id)
    # print(f"The job with id {job_id} is {job}.")
    # job_id = 1
    # job = db.session.query(Job).get(job_id)
    # job.assigned_to = 1
    # db.session.commit()
    #
    # display_jobs()
    # assign_job(1234, 1, 'aryan@buyer')
    # cancel_job(1234, 1, 'aryan@buyer')
    order_completed(order_tag=1234, seller_id=1, buyer_email='aryan@buyer', rating=5)
    # get_reviews(seller_id=1)
    # jobs = Job.query.all()
    # for job in jobs:
    #     print(job)

@app.route('/')
def index():
    return render_template('sellerCheckjob.html')



