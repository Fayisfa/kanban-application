from flask import Flask, render_template, request
from flask import current_app as app
from backend.models import *


@app.route("/")  # it refers url 127.0.0.1:5000
def home():
    return "<h2> Welocome to Kanban App</h2>"


@app.route("/login", methods=["GET","POST"])
def user_login():
    if request.method == "POST":
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        usr = User_Info.query.filter_by(user_name=uname, pwd =pwd).first() #get first existing user
        if usr and usr.role==0:
            return render_template("admin_dashboard.html",user= usr.user_name)
        # elif usr and usr.role == 1:
        #     return render_template("user_dashboard.html",user= usr.user_name)
        else:
            return render_template("login.html",msg="invalid credentials!")
    return render_template("login.html",msg="")


@app.route("/register",methods=["GET","POST"])
def user_register():
    if request.method == "POST":
        email = request.form.get("email")
        full_name = request.form.get("full_name")
        uname = request.form.get("uname")
        pwd = request.form.get("pwd")
        usr = User_Info.query.filter_by(user_name=uname, pwd =pwd).first() #get first existing user
        if not usr:
            new_user = User_Info(email=email,full_name=full_name,user_name=uname,pwd=pwd)
            db.session.add(new_user)
            db.session.commit()
            return render_template("login.html",msg="")
        else:
            return render_template("signup.html",msg="user already exist!")
    
    return render_template("signup.html")


#UDF for reading all users

def fetch_users():
    users = User_Info.query.filter_by(role=1).all()
    user_list = {}
    for user in users:
        if user.id not in user_list.keys():
            user_list[user.id] = [user.use]

# more routes
