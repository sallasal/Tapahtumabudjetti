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
    user_payment_total = payments.user_payment_total(users.user_id(), id)
    count_payments = payments.count_payments(id)
    if creator_id == users.user_id():
        return render_template("project.html", project_information = project_information, user_information = user_information, subproject_list = subproject_list, category_list = category_list, other_payment_list = other_payment_list, user_payment_list = user_payment_list, grandtotal = grandtotal, payment_grandtotal = payment_grandtotal, user_payment_total=user_payment_total, count_payments=count_payments)
    else:
        return render_template("projectguest.html", project_information = project_information, user_information = user_information, subproject_list = subproject_list, category_list = category_list, other_payment_list = other_payment_list, user_payment_list = user_payment_list, grandtotal = grandtotal, payment_grandtotal = payment_grandtotal,user_payment_total=user_payment_total)

#Route for creating new project and form page for this
@app.route("/createproject", methods=["GET","POST"])
def createproject():
    if request.method == "GET":
        return render_template("createproject.html")
    if request.method == "POST":
        name = request.form["name"]
        if len(name) < 3 or len(name) > 100:
            return render_template("error.html",message="Väärän pituinen nimi. Tapahtuman nimen on oltava 3–100 merkkiä pitkä.")
        project_id = projects.add_project(name)
        if project_id != None:
            return render_template("created.html", project_id = project_id)
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
    if total_sum == '':
        return render_template("error.html", message="Uutta osa-aluetta ei voi lisätä ilman summaa. Lisää summa.")
    if len(name) < 3 or len(name) > 100:
        return render_template("error.html", message="Virheellinen osa-alueen nimi. Osa-alueen nimen on oltava 3–100 merkkiä pitkä.")
    if subprojects.add_subproject(name,total_sum,project_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Osa-alueen lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

# Route for allowing user to edit subproject values
@app.route("/editsubprojects/<int:id>", methods=["GET"])
def editsubprojects(id):
    project_information = projects.get_project(id)
    subproject_list = subprojects.list_subprojects(id)
    getid = projects.get_userid(id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if not userid1 == userid2:
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

# Route for listing all payments in one subproject
@app.route("/subprojectpayments/<int:subproject_id>", methods=["POST"])
def subprojectpayments(subproject_id):
    project_id = request.form["project_id"]
    subproject_name = request.form["subproject_name"]
    subproject_total = request.form["subproject_total"]
    payments_in_subproject = subprojects.payments_in_subproject(subproject_id)
    getid = projects.get_userid(project_id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if userid1 != userid2:
        return render_template("error.html", message="Vain tapahtuman järjestäjä voi tarkastella budjetin osa-alueisiin liitettyjä maksuja.")
    else:
        return render_template("subprojectpayments.html", payments_in_subproject=payments_in_subproject, subproject_name=subproject_name, project_id=project_id, subproject_total=subproject_total)

# -----
# CATEGORY ROUTES
# -----

# Route for adding new category to db
@app.route("/addcategory", methods=["POST"])
def addcategory():
    project_id = request.form["project_id"]
    name = request.form["name"]
    if len(name) < 3 or len(name) > 100:
        return render_template("error.html",message="Virheellinen kategorian nimi. Nimessä on oltava 3–100 merkkiä.")
    if categories.add_category(name,project_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Kategorian lisääminen ei onnistunut. Tarkista arvot ja yritä uudelleen.")

# Route for listing all payments in one category
@app.route("/categorypayments/<int:category_id>", methods=["POST"])
def categorypayments(category_id):
    project_id = request.form["project_id"]
    category_name = request.form["category_name"]
    payments_in_category = categories.payments_in_category(category_id)
    category_total = categories.category_total(category_id)
    getid = projects.get_userid(project_id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if not userid1 == userid2:
        return render_template("error.html", message="Vain tapahtuman järjestäjä voi tarkastella kategoriaan liitettyjä maksuja.")
    else:
        return render_template("categorypayments.html", category_name=category_name, project_id=project_id, payments_in_category=payments_in_category, category_total=category_total)

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
    if date == '':
        return render_template("error.html", message="Lisää maksulle päivämäärä.")
    if len(recipient) < 3 or len(recipient) > 100:
        return render_template("error.html", message="Vastaanottaja-kentän arvon pituuden on oltava 3–100 merkkiä.")
    if len(message) > 100:
        return render_template("error.html", message="Viesti ei voi olla yli 100 merkkiä pitkä.")
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
    project_id = request.form["project_id"]
    if payments.delete_payment(payment_id):
        return redirect("/project/"+project_id)
    else:
        return render_template("error.html",message="Maksun poistaminen ei onnistunut.")

# Route for listing payments by date, oldest first
@app.route("/paymentsbydate/<int:id>", methods=["POST"])
def paymentsbydate(id):
    project_id = request.form["project_id"]
    payments_by_date = payments.payments_by_date(id)
    return render_template("paymentsbydate.html", payments_by_date=payments_by_date, project_id=project_id)

# Route for listing payments by date, newest first
@app.route("/paymentsbydatedesc/<int:id>", methods=["POST"])
def paymentsbydatedesc(id):
    project_id = request.form["project_id"]
    payments_by_date_desc = payments.payments_by_date_desc(id)
    return render_template("paymentsbydatedesc.html", payments_by_date_desc=payments_by_date_desc, project_id=project_id)

#Route for listing payments before defined date
@app.route("/paymentsbeforedate", methods=["GET"])
def paymnetsbeforedate():
    project_id = request.args["project_id"]
    date = request.args["enddate"]
    getid = projects.get_userid(project_id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if userid1 != userid2:
        return render_template("error.html", message="Vain tapahtuman järjestäjä voi listata maksut.")
    if date == '':
        return render_template("error.html",message="Syötä päivämäärä, jota varhaisemmat maksut listataan.")
    paymentsbeforedate = payments.paymentsbeforedate(project_id,date)
    return render_template("paymentsbeforedate.html", paymentsbeforedate = paymentsbeforedate, project_id=project_id)

# Route for listing payments after defined date
@app.route("/paymentsafterdate", methods=["GET"])
def paymentsafterdate():
    project_id = request.args["project_id"]
    date = request.args["enddate"]
    getid = projects.get_userid(project_id)
    userid1 = getid[0]
    userid2 = users.user_id()
    if userid1 != userid2:
        return render_template("error.html",message="Vain tapahtuman järjestäjä voi listata maksut.")
    if date == '':
        return render_template("error.html",message="Syötä päivämäärä, jota varhaisemmat maksut listataan.")
    paymentsafterdate = payments.paymentsafterdate(project_id,date)
    return render_template("paymentsafterdate.html", paymentsafterdate = paymentsafterdate, project_id=project_id)

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
        if len(username) < 3 or len(username) > 100:
            return render_template("error.html",message="Tarkista käyttäjänimi. Käyttäjänimessä on oltava 3–100 merkkiä.")
        if len(password) < 5 or len(username) > 100:
            return render_template("error.html",message="Tarkista salasana. Salasanassa on oltava 5–100 merkkiä.")
        if len(email) < 5 or len(email) > 100:
            return render_template("error.html",message="Tarkista sähköpostiosoite. Sähköpostiosoitteessa on oltava 5–100 merkkiä.")
        if users.register(username,password,email):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut. Kokeile toista nimimerkkiä.")
