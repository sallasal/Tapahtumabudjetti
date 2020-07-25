from app import app
import tapahtumat, users
from flask import render_template, redirect, session, request

# Avaussivun reititys
@app.route("/")
def index():
    laskuri = tapahtumat.laske_tapahtumat()
    tapahtumalista = tapahtumat.listaa_tapahtumat()
    return render_template("index.html", laskuri = laskuri, tapahtumalista = tapahtumalista)


# Kirjautumiseen liittyvät reitit
@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("/login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        if users.register(username,password,email):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut. Kokeile toista nimimerkkiä.")
