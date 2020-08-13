from db import db
import users

# Add new payment information to db
def add_payment(recipient,total,paymentsubproject,category_list,date,message):
    userid = users.user_id()
    sql = "INSERT INTO payments (userid, subproject, recipient, total, date, message) VALUES (:userid,:subproject,:recipient,:total,:date,:message) RETURNING id"
    result = db.session.execute(sql, {"userid":userid,"subproject":paymentsubproject,"recipient":recipient,"total":total,"date":date,"message":message})
    payment_id = result.fetchone()[0]
    db.session.commit()
    for category in category_list:
        category_sql = "INSERT INTO paymentcategory (payment_id,category_id) VALUES (:payment_id,:category_id)"
        db.session.execute(category_sql, {"payment_id":payment_id,"category_id":int(category)})
    db.session.commit()
    return True

# List all payments from project, includes names of payment owner and subproject of the payment
def list_payments(project_id):
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id)"
    result = db.session.execute(sql, {"project_id":project_id})
    payment_list = result.fetchall()
    return payment_list

# List all payments from project that are own by user logged in, includes name of subproject of the payment
def list_user_payments(project_id):
    user_id = users.user_id()
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name, p.id FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id) AND p.userid=:user_id"
    result = db.session.execute(sql, {"project_id":project_id,"user_id":user_id})
    user_payment_list = result.fetchall()
    return user_payment_list

# List all payments from project that are NOT own by user logged in, includes names payment owner and subproject of the payment
def list_other_payments(project_id):
    user_id = users.user_id()
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id) AND NOT p.userid=:user_id"
    result = db.session.execute(sql, {"project_id":project_id,"user_id":user_id})
    other_payment_list = result.fetchall()
    return other_payment_list

# Calculate total sum of subproject budgets for defined project
def get_payment_grandtotal(project_id):
    sql = "SELECT SUM(p.total) FROM payments p LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id)"
    result = db.session.execute(sql, {"project_id":project_id})
    payment_grandtotal = result.fetchone()[0]
    return payment_grandtotal

# Delete payment from paymentcategories and then from payments
def delete_payment(payment_id):
    sql_paymentcategory = "DELETE FROM paymentcategory WHERE payment_id=:payment_id"
    db.session.execute(sql_paymentcategory, {"payment_id":payment_id})
    db.session.commit()
    sql_payments = "DELETE FROM payments WHERE id=:payment_id"
    db.session.execute(sql_payments, {"payment_id":payment_id})
    db.session.commit()
    return True

# List by date all payments from project, includes names of payment owner and subproject of the payment
def payments_by_date(project_id):
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name, p.id FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id) ORDER BY p.date"
    result = db.session.execute(sql, {"project_id":project_id})
    payments_by_date = result.fetchall()
    return payments_by_date
