from flask import  render_template, request, redirect, url_for, flash
from flask import Flask
from sqlalchemy.sql import func
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

DB_NAME = "database.db"
db = SQLAlchemy()
app.config["SECRET KEY"] = "DSHSHSFHAHF HSFHSKHFS"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "jlsjfl"
db.init_app(app=app)

class Buyer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phoneNo = db.Column(db.String(100))
    address = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.name} {self.id} {self.email} {self.password}"

class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phoneNo = db.Column(db.String(100))
    address = db.Column(db.String(100))
    experience = db.Column(db.String(100))

    def __repr__(self) -> str:
        return f"{self.name} {self.id} {self.email} {self.password}"
# class Job(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     data = db.Column(db.String(10000))
#     date = db.Column(db.DateTime(timezone=True), default=func.now())
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#

with app.app_context():
    db.create_all()
# sellers = Seller.query.all()
# print(sellers)


def user_login(email, password):

    try:
        user = Seller.query.filter_by(email=email).first()
        user_type = 'Seller'
    except:
        user = Buyer.query.filter_by(email=email).first()
        user_type = 'Buyer'
    if user:
        if check_password_hash(user.password, password):
            flash('Logged in successfully!', category='success')

            if user_type == 'Seller':
                return redirect(url_for('seller_home'))
            return redirect(url_for('buyer_home'))
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Email does not exist.', category='error')

def user_signup(db, username, password1, password2, address, experience, phoneNo, email, User):

    user = Seller.query.filter_by(email=email).first()

    if user:
        flash('Email already exists.', category='error')
        return render_template(url_for('login'))

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
            flash('Email already exists.', category='error')
            return render_template(url_for('login'))
        if User == 'Seller':
            new_user = Seller(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), experience=experience, phoneNo=phoneNo, address=address)
        elif User == 'Buyer':
            new_user = Buyer(email=email, name=username, password=generate_password_hash(
                password1, method='sha256'), phoneNo=phoneNo, address=address)

        db.session.add(new_user)
        db.session.commit()
        flash('Account created!', category='success')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('buyer_base.html')

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
        user_signup(username=seller_username, db=db, User='Seller', password1=seller_password1, password2=seller_password2, address=seller_address, phoneNo=seller_phoneNo, experience=seller_experience, email=seller_email)
        # return redirect(url_for('seller_home'))
        #
        # print(seller_phoneNo, seller_password, seller_email, seller_username, seller_address, seller_experience)
        return redirect(url_for('hello_world'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        print(email, password)
        user_login(email=email, password=password)

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)
