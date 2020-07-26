from app import app
import tapahtumat, users
from flask import render_template, redirect, session, request

# Sivujen reititykset
@app.route("/")
def index():
    laskuri = tapahtumat.laske_tapahtumat()
    tapahtumalista = tapahtumat.listaa_tapahtumat()
    return render_template("index.html", laskuri = laskuri, tapahtumalista = tapahtumalista)

@app.route("/createtapahtuma", methods=["GET","POST"])
def createtapahtuma():
    if request.method == "GET":
        return render_template("createtapahtuma.html")
    if request.method == "POST":
        nimi = request.form["nimi"]
        if tapahtumat.lisaa_tapahtuma(nimi):
            return redirect("/")
        else:
            return render_template("error.html",message="Tapahtuman luominen ei jostain syystä onnistunut. Tarkista arvo ja yritä uudelleen.")

@app.route("/tapahtuma/<int:id>", methods=["GET"])
def tapahtuma(id):
    tapahtumatiedot = tapahtumat.hae_tapahtuma(id)
    return render_template("tapahtuma.html", tapahtumatiedot = tapahtumatiedot)

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
