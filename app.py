from datetime import datetime
import os
from flask import Flask, flash, make_response, redirect, render_template, request, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm  # Import FlaskForm
from wtforms import StringField, SubmitField, IntegerField # Import StringField and SubmitField
from wtforms.validators import DataRequired, Email
from models import Order, Order1, User, UserModel, db
from forms import LoginForm, UserDataForm, userForm
from products.data import get_products


PEOPLE_FOLDER = os.path.join('static', 'images')
# create Flask instance
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

db.init_app(app)

def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

# create route decorato

# @app.route("/user/<name>")
# def user(name):
#     return render_template("user.html", name=name)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = UserDataForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = UserModel(
                name=form.name.data, 
                username=form.username.data,
                phone=form.phone.data,
                email=form.email.data, 
                password=form.password.data,
                )
            db.session.add(user)
            db.session.commit()
        form.name.data=''
        form.email.data=""
        form.username.data=''
        form.phone.data=''
        form.password.data=''
        flash("user addes successfully")
        return redirect(url_for('login'))
    else:
        print("else")
    our_users = UserModel.query.order_by(UserModel.id)

    return render_template("register.html", 
        form=form,             
        our_users=our_users
                           )

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = UserModel.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            # Create a response object
            response = make_response(redirect(url_for('dashboard')))
            # Set cookies
            response.set_cookie('user_id', str(user.id))
            response.set_cookie('user_email', user.email)
            # Flash a success message
            flash("Login successful!", "success")
            return response
        else:
            print("hacbjha")
            flash("Invalid email or password", "error")
    return render_template('login.html', form=form)

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    search_query = request.args.get('query', None)
    category = request.args.get('category', default=None)
    products = get_products(category=category, search_query=search_query)
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'background.png')
    return render_template('dashboard.html', image_urls=full_filename, products=products)

@app.route("/cart")
def cart():
    return render_template("user.html")

@app.route("/contact")
def contact():
    return render_template("contact_us.html")

@app.route("/user/add", methods=["GET", "POST"])
def adduser():
    name = None
    form = userForm()
    if form.validate_on_submit():
        print("user", form.email.data)
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(name=form.name.data, email=form.email.data, password="1234")
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data=''
        form.email.data=""
        flash("user addes successfully")
    else:
        print("else")
    our_users = User.query.order_by(User.id)
    return render_template("add_user.html", form=form, name=name,
                           our_users=our_users
                       )


@app.route('/cart_data', methods=['POST'])
def cart_data():
    # Retrieve user email and id from cookies
    user_email = request.cookies.get('user_email')
    user_id = request.cookies.get('user_id')
    
    if not user_email or not user_id:
        return jsonify({"error": "User not authenticated"}), 401
    
    # Ensure user_id is an integer
    user_id = int(user_id)

    data = request.json
    cart_items = request.json.get('cart_items', [])
    for item in cart_items:
        item['price'] = float(item['price'])
    print("card", cart_items)
    for item in cart_items:
        cart_item = Order1(
            customer_email=user_email,
            # user_id=user_id,
            pname=item['name'],
            pdescription=item['description'],
            pprice=item['price'],
            porder_date=datetime.utcnow() # Use current date and time
        )
        db.session.add(cart_item)
    db.session.commit()
    return render_template('user.html', cart_items=cart_items)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    # Set the cookies' expiration date to a past date to remove them
    response.set_cookie('user_email', '', expires=0)
    response.set_cookie('user_id', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
