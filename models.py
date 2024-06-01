from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)
    stock_quantity = db.Column(db.Integer, nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(100), nullable=False)
    # user_id = db.Column(db.Integer, nullable=False)
    pname = db.Column(db.String(100), nullable=False)
    pdescription = db.Column(db.Text, nullable=False)
    pprice = db.Column(db.Float, nullable=False)
    pstock_quantity = db.Column(db.Integer, nullable=False)
    pimage_url = db.Column(db.String(200), nullable=False)
    porder_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


class Order1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_email = db.Column(db.String(100), nullable=False)
    pname = db.Column(db.String(100), nullable=False)
    pdescription = db.Column(db.Text, nullable=False)
    pprice = db.Column(db.Float, nullable=False)
    porder_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)  # Changed from db.Float to db.String
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):  
        return '<User %r>' % self.name

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)  # Changed from db.Float to db.String
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):  
        return '<User %r>' % self.name
    
