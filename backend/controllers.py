from flask import Flask,render_template
from flask import current_app as app 


@app.route("/") # it refers url 127.0.0.1:5000
def home():
    return "<h2> Welocome to Kanban App</h2>"

@app.route("/login")
def user_login():
    return render_template("login.html")

@app.route("/register")
def user_register():
    return render_template("signup.html")




#more routes