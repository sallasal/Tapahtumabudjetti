from app import app
import tapahtumat
from flask import render_template, redirect, session, request

@app.route("/")
def index():
    laskuri = tapahtumat.laske_tapahtumat()
    return render_template("index.html", laskuri = laskuri)

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    session["username"] = username
    return redirect("/")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")
