from app import app
import categories, payments, projects, subprojects, users
from flask import render_template, redirect, session, request

# Route for index page
@app.route("/")
def index():
    counter = projects.count_projects()
    project_list = projects.list_projects()
    user_id = users.user_id()
    user_project_list = projects.list_user_projects(user_id)
    other_projects_list = projects.list_other_projects(user_id)
    return render_template("index.html", counter = counter, project_list = project_list, user_project_list = user_project_list, other_projects_list = other_projects_list)

# -----
# PROJECT ROUTES
# -----

# Route for project pages for every project
@app.route("/project/<int:id>", methods=["GET"])
def project(id):
    project_information = projects.get_project(id)
    creator_id = project_information[2]
    user_information = users.user_name(creator_id)
    subproject_list = subprojects.list_subprojects(id)
    category_list = categories.list_categories(id)
    other_payment_list = payments.list_other_payments(id)
    user_payment_list = payments.list_user_payments(id)
    grandtotal = subprojects.get_grandtotal(id)
    payment_grandtotal = payments.get_payment_grandtotal(id)
    print(id)
    print(subproject_list)
    if creator_id == users.user_id():
        return render_template("project.html", project_information = project_information, user_information = user_information, subproject_list = subproject_list, category_list = category_list, other_payment_list = other_payment_list, user_payment_list = user_payment_list, grandtotal = grandtotal, payment_grandtotal = payment_grandtotal)
    else:
        return render_template("projectguest.html", project_information = project_information, user_information = user_information, subproject_list = subproject_list, category_list = category_list, other_payment_list = other_payment_list, user_payment_list = user_payment_list, grandtotal = grandtotal, payment_grandtotal = payment_grandtotal)

#Route for creating new project and form page for this
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

# -----
# SUBPROJECT ROUTES
# -----

# Route for creating new subproject
@app.route("/createsubproject", methods=["POST"])
def createsubproject():
    project_id = request.form["tapahtumaid"]
    name = request.form["name"]
    total_sum = request.form["total_sum"]
    if subprojects.add_subproject(name,total_sum,project_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Osa-alueen lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

# Route for allowing user to edit subproject values
@app.route("/editsubprojects/<int:id>", methods=["GET"])
def editsubprojects(id):
    allow = False
    project_information = projects.get_project(id)
    subproject_list = subprojects.list_subprojects(id)
    getid = projects.get_userid(id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if userid1 == userid2:
        allow = True
    if not allow:
        return render_template("error.html", message="Ei oikeutta muokata osa-alueita. Vain tapahtuman järjestäjällä on oikeus muokata osa-alueita ja kategorioita.")
    else:
        return render_template("editsubprojects.html", project_information = project_information, subproject_list = subproject_list)

# Route for update subproject values in db
@app.route("/updatetotal", methods=["POST"])
def updatetotal():
    project_id = request.form["project_id"]
    subproject_id = request.form["subproject_id"]
    newtotal = request.form["newtotal"]
    if subprojects.update_total(subproject_id,newtotal):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html", message="Osa-alueen päivittäminen ei onnistunut.")

# -----
# CATEGORY ROUTES
# -----

# Route for adding new category to db
@app.route("/addcategory", methods=["POST"])
def addcategory():
    project_id = request.form["project_id"]
    name = request.form["name"]
    if categories.add_category(name,project_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Kategorian lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

# Route for listing all payments in one category
@app.route("/categorypayments/<int:category_id>", methods=["POST"])
def categorypayments(category_id):
    allow = False
    project_id = request.form["project_id"]
    category_name = request.form["category_name"]
    payments_in_category = categories.payments_in_category(category_id)
    getid = projects.get_userid(project_id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if userid1 == userid2:
        allow=True
    if not allow:
        return render_template("error.html", message="Vain tapahtuman järjestäjä voi tarkastella kategoriaan liitettyjä maksuja.")
    else:
        return render_template("categorypayments.html", category_name=category_name, project_id=project_id, payments_in_category=payments_in_category)

# -----
# PAYMENT ROUTES
# -----

# Route for page and form to adding payment
@app.route("/addpayment", methods=["POST"])
def addpayment():
    project_id = request.form["project_id"]
    recipient = request.form["recipient"]
    total = request.form["total"]
    date = request.form["paymentdate"]
    message = request.form["message"]
    paymentsubproject = -1
    if "paymentsubproject" in request.form:
        paymentsubproject = request.form["paymentsubproject"]
    category_list = request.form.getlist("paymentcategory")
    if paymentsubproject is not -1 and payments.add_payment(recipient,total,paymentsubproject,category_list,date,message):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Maksun lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

# Route for creating a new category in project
@app.route("/createpayment/<int:id>", methods=["GET"])
def createpayment(id):
    project_information = projects.get_project(id)
    subproject_list = subprojects.list_subprojects(id)
    category_list = categories.list_categories(id)
    return render_template("createpayment.html", project_information = project_information, subproject_list = subproject_list, category_list = category_list)

# Route for deleting payment first from paymentcategories, then from payments
@app.route("/deletepayment", methods=["POST"])
def deletepayment():
    payment_id = request.form["payment_id"]
    print(payment_id)
    project_id = request.form["project_id"]
    if payments.delete_payment(payment_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Maksun poistaminen ei onnistunut.")

# -----
# USER AND SESSION ROUTES
# -----

# Route for credential check and starting new session
@app.route("/login", methods=["GET","POST"])
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

# Route for ending session
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

# Route for registering new user credentials
@app.route("/register", methods=["GET","POST"])
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
