from app import app
import projects, subprojects, users
from flask import render_template, redirect, session, request

# Sivujen reititykset
@app.route("/")
def index():
    counter = projects.count_projects()
    project_list = projects.list_projects()
    return render_template("index.html", counter = counter, project_list = project_list)

@app.route("/createproject", methods=["GET","POST"])
def createproject():
    if request.method == "GET":
        return render_template("createproject.html")
    if request.method == "POST":
        nimi = request.form["nimi"]
        if projects.add_project(nimi):
            return redirect("/")
        else:
            return render_template("error.html",message="Tapahtuman luominen ei jostain syystä onnistunut. Tarkista arvo ja yritä uudelleen.")

@app.route("/project/<int:id>", methods=["GET"])
def project(id):
    tapahtumatiedot = projects.get_project(id)
    jarjestaja_id = tapahtumatiedot[2]
    kayttajatiedot = users.user_name(jarjestaja_id)
    return render_template("project.html", tapahtumatiedot = tapahtumatiedot, kayttajatiedot = kayttajatiedot)

#Osaprojekteihin liittyvät reititykset
@app.route("/createsubproject", methods=["POST"])
def createsubproject():
    tapahtumaid = request.form["tapahtumaid"]
    nimi = request.form["nimi"]
    budjettisumma = request.form["budjettisumma"]
    if subprojects.add_subproject(nimi,budjettisumma,tapahtumaid):
        return redirect("/project/"+tapahtumaid)
    else:
        return render_template("error.html",message="Osa-alueen lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

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
