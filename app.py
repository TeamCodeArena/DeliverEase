from flask import render_template, request, redirect, url_for, flash, session
from flask import Flask
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user,UserMixin, login_required, logout_user, current_user
from flask_login import LoginManager
import random

app = Flask(__name__)


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db = SQLAlchemy(app)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "jlsjfl"
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
    otp = db.Column(db.Integer, default='NIL')
    review = db.Column(db.String(100), default='N/A')
    def __repr__(self) -> str:
        return f"Job ID: {self.id} Job Status: {self.status} Job Review: {self.review} Item Type: {self.product_type} Pickup Address: {self.pickup_address} Job Created: {self.date} Job OrderTag: {self.order_tag} Pickup Time:{self.pickup_time} Delivery Address: {self.delivery_address} Delivery Time: {self.delivery_time} Delivery Pincode: {self.delivery_pincode} Pickup Pincode: {self.pickup_pincode} Created By: {self.created_by} Assigned_To: {self.assigned_to}"

otp = []

with app.app_context():
    db.create_all()
    # new_buyer = Buyer(email='test@234123wrqw', name='username', password='password123', phoneNo='1234567890', address='123 Main St')
    # db.session.add(new_buyer)
    #
    # db.session.commit()

    # new_job = Job(pickup_pincode='110034', delivery_pincode='110035', pickup_address='street2', pickup_time='11:00 AM',
    #               delivery_address='456 West', delivery_time='12:00AM ',buyer_id = 1)
    # db.session.add(new_job)
    # db.session.commit()
    #
    # new_job = Job(pickup_pincode='110006', delivery_pincode='11009', pickup_address='Street random', pickup_time='12:00 AM', delivery_address='west zone Pitampura metro', delivery_time='2:00AM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()
    #
    #
    # new_job = Job(pickup_pincode='110099', delivery_pincode='110056', pickup_address='chandi chowk parathewali gali', pickup_time='12:00 PM', delivery_address='okhala metro', delivery_time='2:00PM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()
    #
    # new_job = Job(pickup_pincode='711302', delivery_pincode='711303', pickup_address='park street', pickup_time='12:00 AM', delivery_address='kolkata central metro', delivery_time='2:00AM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()
    #
    # new_job = Job(pickup_pincode='731302', delivery_pincode='711403', pickup_address='pragati maidan', pickup_time='13:00 AM', delivery_address='bagbazar', delivery_time='4:00AM',buyer_id=1)
    # db.session.add(new_job)


    # new_job = Job(pickup_pincode='711322', delivery_pincode='711303', pickup_address='mere ghar se', pickup_time='12:00 AM', delivery_address='kolkata central metro', delivery_time='2:00AM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()
    #
    # new_job = Job(pickup_pincode='732302', delivery_pincode='711403', pickup_address='kahi se', pickup_time='13:00 AM', delivery_address='bagbazar', delivery_time='4:00AM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()
    # jobs = Job.query.all()
    # if not jobs:
    #     print('Absent')
    # for job in jobs:
    #     print(job)
# sellers = Seller.query.all()
# print(sellers)

# def search_jobs():
#     jobs

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
    for seller_review in seller_reviews:
        print(seller_review.rating)
        print(seller_review.review)


def get_jobs():
    num_jobs = Job.query.filter_by(assigned_to=0).order_by(func.random()).limit(5).all()
    job1 = {}
    job2 = {}
    job3 = {}
    job4 = {}
    job5 = {}
    job_ids = []
    for job in num_jobs:
        job_ids.append(job.id)
    for x in range(6):
    # job_id = 1
        buyer = db.session.query(Buyer).join(Job).filter(Job.id == job_id).first()
        job = Job.query.get(job_id)
        # print(job, buyer)
        if x == 1:
            job1 = {

                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }

        elif x == 2:
            job2 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 3:
            job3 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 4:
            job4 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 5:
            job5 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        # print(job5)
    return job1, job2, job3, job4, job5




def user_login(email, password):


    user = Seller.query.filter_by(email=email).first()
    user_type = 'Seller'
    if not user:
        user = Buyer.query.filter_by(email=email).first()
        user_type = 'Buyer'
    print(user_type, user)
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in successfully!', category='success')
            if user_type == 'Seller':
                url = url_for('seller_home')

            if user_type == 'Buyer':
                url = url_for('buyer_home')
            return url
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Account does not exist.', category='error')

def user_signup(username, password1, password2, address, phoneNo, email, user_type, experience='None'):
    if user_type == 'Seller':
        user = Seller.query.filter_by(email=email).first()
    elif user_type == 'Buyer':
        user = Buyer.query.filter_by(email=email).first()

    if user:

        flash('Account already exists.', category='error')
        url = url_for('login', email=email)
        return url

    elif len(email) < 4:
        flash('Email must be greater than 3 characters.', category='error')
    elif len(username) < 2:
        flash('First name must be greater than 1 character.', category='error')
    elif len(password1) < 7:
        flash('Password must be at least 7 characters.', category='error')
    elif password1 != password2:
        flash('Passwords don\'t match.', category='error')
    else:
        if user_type == 'Seller':
            new_user = Seller(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), experience=experience, phoneNo=phoneNo, address=address)
        elif user_type == 'Buyer':
            new_user = Buyer(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), phoneNo=phoneNo, address=address)

        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')
        if user_type == 'Seller':
            url = url_for('seller_home', email=email)

        elif user_type == 'Buyer':
            url = url_for('buyer_home', email=email)
        print(url)
        return url
# @app.route('/logout')
# # @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('auth.login'))
@app.route('/')
def index_page():  # put application's code here
    return render_template('index.html') ## change to index.html

@app.route('/seller_signup', methods=['GET', 'POST'])
def seller_signup():
    if request.method == 'GET':
        return render_template('signUp.html')
    elif request.method == 'POST':

        seller_username = request.form.get('fullName')
        seller_email = request.form.get('email')
        seller_password1 = request.form.get('password')
        seller_password2 = request.form.get('confirmPassword')
        seller_phoneNo = request.form.get('phoneNo')
        seller_address = request.form.get('address')
        seller_experience = request.form.get('workExperience')
        session['email'] = email
        url = user_signup(user_type='Seller', username=seller_username,  password1=seller_password1, password2=seller_password2, address=seller_address, phoneNo=seller_phoneNo, experience=seller_experience, email=seller_email)
        return redirect(url, email=email)

@app.route('/about_us')
def aboutus():
    return render_template('aboutus.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        url = user_login(email=email, password=password)
        session['email'] = email
        return  redirect(url)
    elif request.method == 'GET':
        return render_template('login.html')

@app.route('/get_started')
def get_started():
    return render_template('buyerorseller.html')


@app.route('/buyer_home')
def buyer_home():
    return render_template('buyer_homepage.html')

@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        print('hi')
        pickup_address = request.form.get('pickup_address')
        pickup_time = request.form.get('pickup_time')
        pickup_date = request.form.get('pickup_date')
        delivery_address = request.form.get('delivery_address')
        delivery_time = request.form.get('delivery_time')
        delivery_date = request.form.get('delivery_date')
        delivery_pincode = request.form.get('delivery_pincode')
        pickup_pincode = request.form.get('pickup_pincode')
        # product_type = request.form.get('product_type')
        email = session['email']
        buyer = Buyer.query.filter_by(email=email).first()
        buyer_id = buyer.id
        new_otp = random.randint(1000, 9999)
        while new_otp not in otp:
            opt.append(new_otp)
        new_job = Job(pickup_address=pickup_address, pickup_time=pickup_time, delivery_address=delivery_address,pickup_pincode=pickup_pincode,
                      delivery_time=delivery_time, created_by=buyer_id, delivery_pincode=delivery_pincode, product_type='product_type', otp=new_otp)
        db.session.add(new_job)
        db.session.commit()
        print(new_job)
        return redirect(url_for('seller_home'))

    return render_template('jobform.html')
@app.route('/seller_home')
def seller_home():
    job1, job2, job3, job4, job5 = get_jobs()
    # print('job5', job5)
    print(job1, job2, job3, job4, job5)
    # print(job_details.items())

    return render_template('sellerhomepage.html', job1=job1, job2=job2, job3=job3, job4=job4, job5=job5)

    # return redirect(url_for('posted_jobs')


@app.route('/jobs')
def posted_jobs():
    job1, job2, job3, job4, job5 = get_jobs()
    # print(job_details.items())

    return render_template('seller_homepage.html', job1=job1, job2=job2, job3=job3, job4=job4, job5=job5)

@app.route('/buyer_signup', methods=['GET', 'POST'])
def buyer_signup():
    if request.method == 'GET':
        return render_template('buyer_signup.html')
    elif request.method == 'POST':

        username = request.form.get('fullName')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirmPassword')
        phoneNo = request.form.get('phoneNo')
        address = request.form.get('address')
        url = user_signup(user_type='Buyer', username=username, password1=password1,
                          password2=password2, address=address, phoneNo=phoneNo, email=email)
        print(url)
        session['email'] = email
        return redirect(url)

@app.route('/check-job', methods=['GET'])
def detailed_job():
    if request.method == 'GET':
        job = request.args.get('job')
        job_dict = eval(job)
        buyer_name = job_dict.get('buyer_name')
        delivery_time = job_dict.get('delivery_time')
        pickup_time = job_dict.get('pickup_time')
        delivery_address = job_dict.get('delivery_address')
        pickup_address = job_dict.get('pickup_address')
        delivery_pincode = job_dict.get('delivery_pincode')
        pickup_pincode = job_dict.get('pickup_pincode')
        delivery_type = job_dict.get('product_type')
        return render_template('sellerCheckjob.html',product_type=delivery_type,  buyer_name=buyer_name, delivery_time=delivery_time, pickup_time=pickup_time, delivery_address=delivery_address, pickup_address=pickup_address, pickup_pincode=pickup_pincode, delivery_pincode=delivery_pincode)

## for seller
@app.route('/order_delivery')
def job_accepted():
    email = session['email']
    job = Job.query.filter_by(email=email, status='In Progress').first()

    return render_template('checkorder.html',otp=job.otp, delivery_address=job.delivery_address,
                           delivery_pincode=job.delivery_pincode, delivery_time=job.delivery_time, seller_name=job.assigned_to,
                           pickup_address=job.pickup_address, pickup_time=job.pickup_time, pickup_pincode=job.pickup_pincode)



@app.route('/order_delivery', methods['GET', 'POST'])
def job_accepted():
    if request.method == 'POST':
        email = session['email']
        job = Job.query.filter_by(email=email, status='In Progress').first()
        otp = request.form.get('OTP')
        rating = request.form.get('rating')
        reveiw = request.form.get('review')
        if otp == job.otp:
            print('Delivery Completed Successfully')
            job.status = 'Completed'
            job.review = reveiew
            job.rating = rating


    return render_template('complete_delivery.html')

@app.route('/my_orders')
def buyer_orders():
    email = session['email']
    buyer = Buyer.query.filter_by(email=email).first()
    num_jobs = Job.query.filter_by(assigned_to=0).order_by(func.random()).limit(5).all()
    job1 = {}
    job2 = {}
    job3 = {}
    job4 = {}
    job5 = {}
    job_ids = []
    for job in num_jobs:
        job_ids.append(job.id)
    for x in range(6):
        # job_id = 1
        buyer = db.session.query(Buyer).join(Job).filter(Job.id == job_id).first()
        job = Job.query.get(job_id)
        # print(job, buyer)
        if x == 1:
            job1 = {

                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }

        elif x == 2:
            job2 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 3:
            job3 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 4:
            job4 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        elif x == 5:
            job5 = {
                "buyer_name": buyer.name,
                "Delivery Type": job.product_type,
                "buyer_email": buyer.email,
                "buyer_phone_no": buyer.phoneNo,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode,
                "Job Tag": job.order_Tag
            }
        # print(job5)
    return render_template('myorders.html', job1=job1, job2=job2, job3=job3, job4=job4, job5=job5)


if __name__ == '__main__':
    app.run(debug=True)
