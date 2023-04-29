from flask import  render_template, request, redirect, url_for, flash
from flask import Flask
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,UserMixin, login_required, logout_user, current_user
from flask_login import LoginManager
import random
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    db = SQLAlchemy(app)
    return app, db

app, db = create_app()



class Seller(db.Model, UserMixin):
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
    pickup_time = db.Column(db.String(100))
    delivery_address = db.Column(db.String(1000))
    delivery_time = db.Column(db.String(100))
    delivery_pincode = db.Column(db.String(100))
    pickup_pincode = db.Column(db.String(100))
    buyer_id = db.Column(db.Integer, db.ForeignKey('buyer.id'))
    assigned_to = db.Column(db.Integer, db.ForeignKey('seller.id'), default=0)

    def __repr__(self) -> str:
        return f"{self.pickup_address} {self.date} {self.pickup_time} {self.delivery_address} {self.delivery_time} {self.delivery_pincode} {self.pickup_pincode} {self.buyer_id} {self.assigned_to}"

# def get_jobs():
#     num_jobs = Job.query.count()
#     print('Num of jobs', num_jobs)
#     job1 = {}
#     job2 = {}
#     job3 = {}
#     job4 = {}
#     job5 = {}
#
#     for x in range(5):
#         job_id = random.randint(1, num_jobs)
#         # print(job_id)
#     # job_id = 1
#         buyer = db.session.query(Buyer).join(Job).filter(Job.id == job_id).first()
#         job = Job.query.get(job_id)
#         # print(job, buyer)
#         if x == 1:
#             job1 = {
#                 "buyer_name": buyer.name,
#                 "delivery_time": job.delivery_time,
#                 "pickup_time": job.pickup_time,
#                 "delivery_address": job.delivery_address,
#                 "pickup_address": job.pickup_address,
#                 "delivery_pincode": job.delivery_pincode,
#                 "pickup_pincode": job.pickup_pincode
#             }
#         elif x == 2:
#             job2 = {
#                 "buyer_name": buyer.name,
#                 "delivery_time": job.delivery_time,
#                 "pickup_time": job.pickup_time,
#                 "delivery_address": job.delivery_address,
#                 "pickup_address": job.pickup_address,
#                 "delivery_pincode": job.delivery_pincode,
#                 "pickup_pincode": job.pickup_pincode
#             }
#         elif x == 3:
#             job3 = {
#                 "buyer_name": buyer.name,
#                 "delivery_time": job.delivery_time,
#                 "pickup_time": job.pickup_time,
#                 "delivery_address": job.delivery_address,
#                 "pickup_address": job.pickup_address,
#                 "delivery_pincode": job.delivery_pincode,
#                 "pickup_pincode": job.pickup_pincode
#             }
#         elif x == 4:
#             job4 = {
#                 "buyer_name": buyer.name,
#                 "delivery_time": job.delivery_time,
#                 "pickup_time": job.pickup_time,
#                 "delivery_address": job.delivery_address,
#                 "pickup_address": job.pickup_address,
#                 "delivery_pincode": job.delivery_pincode,
#                 "pickup_pincode": job.pickup_pincode
#             }
#         elif x == 5:
#             job5 = {
#                 "buyer_name": buyer.name,
#                 "delivery_time": job.delivery_time,
#                 "pickup_time": job.pickup_time,
#                 "delivery_address": job.delivery_address,
#                 "pickup_address": job.pickup_address,
#                 "delivery_pincode": job.delivery_pincode,
#                 "pickup_pincode": job.pickup_pincode
#             }
#         print(job1)
#     return job1, job2, job3, job4, job5


with app.app_context():
    db.create_all()

    # # Create a new buyer
    # new_buyer = Buyer(email='test@234123wrqw', name='username', password='password123', phoneNo='1234567890', address='123 Main St')
    # db.session.add(new_buyer)
    #
    # db.session.commit()
    # #
    # # Create a new job and associate it with the buyer
    # for x in range(5):
    #     new_job = Job(pickup_pincode='2323432', delivery_pincode='sfhshffh', pickup_address='123 Elm St', pickup_time='10:00 AM', delivery_address='456 Oak St', delivery_time='1:00 PM', buyer_id=1)
    #     db.session.add(new_job)
    #     db.session.commit()

    # Get the buyer ID from the job ID
    # job_id = 1
    # buyer2 = db.session.query(Buyer).join(Job).filter(Job.id == job_id).first()
    # buyer_address = buyer2.address
# for x in range(10):
#     num = random.randint(0, 2)
#     print(num)

    # print(f"The buyer address associated with job ID {job_id} is {buyer_address}.")
    # get_jobs()
    #
# print(buyer_address)
#     job_id = 1
#     job = db.session.query(Job).get(job_id)
#     job.pickup_address = 'new_pickup_address'
#     db.session.commit()
#     Joba = db.session.query(Job).get(job_id)
# print('printing job', Joba)

# @app.route('/')
# def seller_homepage():
#     job1, job2,  job3, job4, job5 = get_jobs()
#     # print(job_details.items())
#     print(job1.items())
#     # for job_id, job_detail in job1.items():
#     #     print(job_details.items())
#     #     print('printing')
#     #     print(job_id)
#     #     print(job_detail[0])
#     return render_template('testhtml2.html', job1=job1, job2=job2, job3=job3, job4=job4, job5=job5)
# @app.route('/check-job', methods=['GET'])
# def detailed_job():
#     if request.method == 'GET':
#         job = request.args.get('job')
#         job_dict = eval(job)
#
#         buyer_name = job_dict.get('buyer_name')
#         delivery_time = job_dict.get('delivery_time')
#         pickup_time = job_dict.get('pickup_time')
#         delivery_address = job_dict.get('delivery_address')
#         pickup_address = job_dict.get('pickup_address')
#         delivery_pincode = job_dict.get('delivery_pincode')
#         pickup_pincode = job_dict.get('pickup_pincode')
#
#         print(f"Buyer Name: {buyer_name}, Delivery Time: {delivery_time}, Pickup Time: {pickup_time}, Delivery Address: {delivery_address}, Pickup Address: {pickup_address}, Delivery Pincode: {delivery_pincode}, Pickup Pincode: {pickup_pincode}")
#
#         return render_template('sellerCheckjob.html', buyer_name=buyer_name, delivery_time=delivery_time, pickup_time=pickup_time, delivery_address=delivery_address, pickup_address=pickup_address, pickup_pincode=pickup_pincode, delivery_pincode=delivery_pincode)

if __name__ == '__main__':
    app.run(debug=True)
