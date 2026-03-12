from app import app
from flask import render_template,url_for,redirect,flash
from app.forms import IndexForm,LoginForm,RegistrationForm,GameForm,UserForm
from flask_login import current_user,login_user,logout_user,login_required
from app import db
import sqlalchemy as sa
from app.models import User
from app.gameFunc import rollFunc


@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
@login_required
def index():
    form=IndexForm()
    if form.validate_on_submit():
        return redirect(url_for("game"))
    return render_template("index.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return url_for("index")
    form = LoginForm()
    if form.validate_on_submit():
        user=db.session.scalar(sa.select(User).where(User.username==form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash("Sign in First.You are not Registered.")
            return redirect(url_for("login"))
        login_user(user,remember=form.remember_me.data)
        return redirect(url_for("index"))
    return render_template('login.html', title='Sign In', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/register",methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form=RegistrationForm()
    if form.validate_on_submit():
        user=User(username=form.username.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You have been registered as a User.")
        return redirect(url_for("login"))
    return render_template("register.html",form=form)

@app.route("/game",methods=["GET","POST"])
@login_required
def game():
    form=GameForm()
    slot_result=None
    complement = None
    X = None
    if form.validate_on_submit():
        user=current_user
        if(form.bet.data>user.amount or user.amount<=0):
            flash("Check your numbers first Brokie")
            return redirect(url_for("game"))
        
        complement,X,new_amount,slot_result=rollFunc(form.bet.data,user.amount)
        user.amount=new_amount
        db.session.commit()
        
    return render_template("game.html",form=form,slot_result=slot_result,complement=complement,X=X)

@app.route("/user",methods=["GET","POST"])
@login_required
def user():
    user=current_user
    form=UserForm()
    if form.validate_on_submit():
        if(form.deposit.data <= 0):
            flash("Don't try fuck with the system or I will fuck you.")
            return redirect(url_for("user"))
        user.amount=form.deposit.data
        flash("Credits updated.")
        db.session.commit()
        return redirect(url_for("user"))
    return render_template("user.html",form=form,credits=user.amount,username=user.username)