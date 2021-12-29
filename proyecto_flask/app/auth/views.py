from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from db import db
from auth.models import User
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__, url_prefix="")

@auth.route("/login", methods = ['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = True if request.form.get('remember') else False

        user = User.query.filter_by(email = email).first()
        password_validation = check_password_hash(user.password, password)
        if not user or not password_validation:
            flash('Check your credentials and try again')
            return redirect('login')
        
        login_user(user, remember = remember_me)
        return redirect('products/show-catalog')

    return render_template('login.html')

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth/login'))

@auth.route("/signup",methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        name = request.form.get('name')

        user = User.query.filter_by(email=email).first()
        if user:
            message = "Error! ya existe el usuario"
            flash(message)
            return redirect(url_for('auth.signup'))
        hash_password = generate_password_hash(password)
        new_user = User(name = name, password = hash_password, email = email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('signup.html')
