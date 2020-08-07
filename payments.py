from db import db
import users

def add_payment(recipient,total,paymentsubproject,category_list,date,message):
    userid = users.user_id()
    sql = "INSERT INTO payments (userid, subproject, recipient, total, date, message) VALUES (:userid,:subproject,:recipient,:total,:date,:message) RETURNING id"
    result = db.session.execute(sql, {"userid":userid,"subproject":paymentsubproject,"recipient":recipient,"total":total,"date":date,"message":message})
    payment_id = result.fetchone()[0]
    print(payment_id)
    db.session.commit()
    for category in category_list:
        category_sql = "INSERT INTO paymentcategory (payment_id,category_id) VALUES (:payment_id,:category_id)"
        db.session.execute(category_sql, {"payment_id":payment_id,"category_id":int(category)})
    db.session.commit()
    return True

def list_payments(project_id):
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id)"
    result = db.session.execute(sql, {"project_id":project_id})
    payment_list = result.fetchall()
    return payment_list

def list_user_payments(project_id):
    user_id = users.user_id()
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id) AND p.userid=:user_id"
    result = db.session.execute(sql, {"project_id":project_id,"user_id":user_id})
    user_payment_list = result.fetchall()
    return user_payment_list

def list_other_payments(project_id):
    user_id = users.user_id()
    sql = "SELECT p.recipient, p.message, p.total, p.date, users.name, s.name FROM payments p LEFT JOIN users ON users.id=p.userid LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id) AND NOT p.userid=:user_id"
    result = db.session.execute(sql, {"project_id":project_id,"user_id":user_id})
    other_payment_list = result.fetchall()
    return other_payment_list

def get_payment_grandtotal(project_id):
    sql = "SELECT SUM(p.total) FROM payments p LEFT JOIN subprojects s ON s.id=p.subproject WHERE subproject IN (SELECT id FROM subprojects WHERE project=:project_id)"
    result = db.session.execute(sql, {"project_id":project_id})
    payment_grandtotal = result.fetchone()[0]
    return payment_grandtotal