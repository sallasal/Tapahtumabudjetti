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
        name = request.form["name"]
        if projects.add_project(name):
            return redirect("/")
        else:
            return render_template("error.html",message="Tapahtuman luominen ei jostain syystä onnistunut. Tarkista arvo ja yritä uudelleen.")

@app.route("/project/<int:id>", methods=["GET"])
def project(id):
    project_information = projects.get_project(id)
    creator_id = project_information[2]
    user_information = users.user_name(creator_id)
    subproject_list = subprojects.list_subprojects(id)
    return render_template("project.html", project_information = project_information, user_information = user_information, subproject_list = subproject_list)

#Osaprojekteihin liittyvät reititykset
@app.route("/createsubproject", methods=["POST"])
def createsubproject():
    project_id = request.form["tapahtumaid"]
    name = request.form["name"]
    total_sum = request.form["total_sum"]
    if subprojects.add_subproject(name,total_sum,project_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Osa-alueen lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

@app.route("/editsubprojects/<int:id>", methods=["GET"])
def editsubprojects(id):
    project_information = projects.get_project(id)
    subproject_list = subprojects.list_subprojects(id)
    return render_template("editsubprojects.html", project_information = project_information, subproject_list = subproject_list)

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
