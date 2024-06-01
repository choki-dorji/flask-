from flask import Flask, flash, redirect, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm  # Import FlaskForm
from wtforms import StringField, SubmitField, IntegerField # Import StringField and SubmitField
from wtforms.validators import DataRequired, Email
from models import db


class LoginForm(FlaskForm):
    email = StringField("email", validators=[DataRequired()])
    password = StringField("name", validators=[DataRequired()])
    submit = SubmitField("Submit")


class userForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UserDataForm(FlaskForm):
    id = db.Column(db.Integer, primary_key=True)
    name = StringField("name", validators=[DataRequired()])
    username = StringField("username", validators=[DataRequired()])
    phone = IntegerField("phone", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    password = StringField("password", validators=[DataRequired()])
    submit = SubmitField("Submit")
