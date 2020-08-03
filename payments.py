from db import db
import users

def add_payment(recipient,total,paymentsubproject,category_list):
    userid = users.user_id()
    sql = "INSERT INTO payments (userid, subproject, recipient, total) VALUES (:userid,:subproject,:recipient,:total)"
    result = db.session.execute(sql, {"userid":userid,"subproject":paymentsubproject,"recipient":recipient,"total":total})
    db.session.commit()
    return True




    sql = "INSERT INTO projects (name, userid) VALUES (:name,:user_id)"
    db.session.execute(sql, {"name":name,"user_id":user_id})
