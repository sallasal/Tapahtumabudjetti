from db import db
import users

def add_payment(recipient,total,paymentsubproject,category_list,date):
    userid = users.user_id()
    sql = "INSERT INTO payments (userid, subproject, recipient, total, date) VALUES (:userid,:subproject,:recipient,:total,:date)"
    result = db.session.execute(sql, {"userid":userid,"subproject":paymentsubproject,"recipient":recipient,"total":total,"date":date})
    db.session.commit()
    return True




    sql = "INSERT INTO projects (name, userid) VALUES (:name,:user_id)"
    db.session.execute(sql, {"name":name,"user_id":user_id})
