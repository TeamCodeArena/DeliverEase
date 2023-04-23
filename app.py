from flask import  render_template, request, redirect, url_for, flash
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

class Buyer(db.Model, UserMixin):
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

    def __repr__(self) -> str:
        return f"{self.pickup_address} {self.date} {self.pickup_time} {self.delivery_address} {self.delivery_time} {self.delivery_pincode} {self.pickup_pincode} {self.buyer_id}"



with app.app_context():
    db.create_all()
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
    # new_job = Job(pickup_pincode='711302', delivery_pincode='711303', pickup_address='maidan', pickup_time='11:00 AM', delivery_address='bagbazar', delivery_time='4:00AM',buyer_id=1)
    # db.session.add(new_job)
    # db.session.commit()

# sellers = Seller.query.all()
# print(sellers)

# def search_jobs():
#     jobs
def get_jobs():
    num_jobs = Job.query.count()
    print('Num of jobs', num_jobs)
    job1 = {}
    job2 = {}
    job3 = {}
    job4 = {}
    job5 = {}

    for x in range(5):
        job_id = random.randint(1, num_jobs)
        # print(job_id)
    # job_id = 1
        buyer = db.session.query(Buyer).join(Job).filter(Job.id == job_id).first()
        job = Job.query.get(job_id)
        # print(job, buyer)
        if x == 1:
            job1 = {
                "buyer_name": buyer.name,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode
            }
        elif x == 2:
            job2 = {
                "buyer_name": buyer.name,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode
            }
        elif x == 3:
            job3 = {
                "buyer_name": buyer.name,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode
            }
        elif x == 4:
            job4 = {
                "buyer_name": buyer.name,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode
            }
        elif x == 5:
            job5 = {
                "buyer_name": buyer.name,
                "delivery_time": job.delivery_time,
                "pickup_time": job.pickup_time,
                "delivery_address": job.delivery_address,
                "pickup_address": job.pickup_address,
                "delivery_pincode": job.delivery_pincode,
                "pickup_pincode": job.pickup_pincode
            }
        print(job1)
    return job1, job2, job3, job4, job5



login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

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
            login_user(user, remember=True)
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
        user = Buyer.query.filter_by(email=email).first()
        if user:
            flash('Account already exists.', category='error')
            return redirect(url_for('login', email=email))
        if user_type == 'Seller':
            new_user = Seller(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), experience=experience, phoneNo=phoneNo, address=address)
        elif user_type == 'Buyer':
            new_user = Buyer(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), phoneNo=phoneNo, address=address)

        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('Account created!', category='success')
        if user_type == 'Seller':
            url = url_for('seller_home')

        elif user_type == 'Buyer':
            url = url_for('buyer_home')
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
        seller_password2 = request.form.get('cofirmPassword')
        seller_phoneNo = request.form.get('phoneNo')
        seller_address = request.form.get('address')
        seller_experience = request.form.get('workExperience')
        url = user_signup(user_type='Seller', username=seller_username,  password1=seller_password1, password2=seller_password2, address=seller_address, phoneNo=seller_phoneNo, experience=seller_experience, email=seller_email)
        return redirect(url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        url = user_login(email=email, password=password)
        return  redirect(url)
    elif request.method == 'GET':
        return render_template('login.html')
@app.route('/buyer_home')
def buyer_home():
    return render_template('buyer_homepage.html')
@app.route('/place_order', methods=['GET', 'POST'])
def place_order():
    if request.method == 'POST':
        pickup_address = request.form.get('pickup_address')
        pickup_time = request.form.get('pickup_time')
        pickup_date = request.form.get('pickup_date')
        delivery_address = request.form.get('delivery_address')
        delivery_time = request.form.get('delivery_time')
        delivery_date = request.form.get('delivery_date')
        delivery_pincode = request.form.get('delivery_pincode')
        pickup_pincode = request.form.get('pickup_pincode')
        print(current_user.id)
        new_job = Job(pickup_address=pickup_address, pickup_time=pickup_time, delivery_address=delivery_address,
                      delivery_time=delivery_time, delivery_pincode=delivery_pincode, buyer_id=current_user.id)
        db.session.add(new_job)
        db.session.commit()
        return redirect(url_for('posted_jobs'))

    return render_template('jobform.html')
@app.route('/seller_home')
def seller_home():
    job1, job2, job3, job4, job5 = get_jobs()
    # print(job_details.items())

    return render_template('seller_homepage.html', job1=job1, job2=job2, job3=job3, job4=job4, job5=job5)

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
        password2 = request.form.get('cofirmPassword')
        phoneNo = request.form.get('phoneNo')
        address = request.form.get('address')
        url = user_signup(user_type='Buyer', username=username, password1=password1, password2=password2, address=address, phoneNo=phoneNo, email=email)
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


        return render_template('sellerCheckjob.html', buyer_name=buyer_name, delivery_time=delivery_time, pickup_time=pickup_time, delivery_address=delivery_address, pickup_address=pickup_address, pickup_pincode=pickup_pincode, delivery_pincode=delivery_pincode)


# login_manager = LoginManager()
# login_manager.login_view = 'login'
# login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    try:
        user = Buyer.query.get(int(id))
    except:
        user = Seller.query.get(int(id))
    return user

if __name__ == '__main__':
    app.run(debug=True)
