from db import db
import users

def add_payment(recipient,total,paymentsubproject,category_list,date):
    userid = users.user_id()
    sql = "INSERT INTO payments (userid, subproject, recipient, total, date) VALUES (:userid,:subproject,:recipient,:total,:date) RETURNING id"
    result = db.session.execute(sql, {"userid":userid,"subproject":paymentsubproject,"recipient":recipient,"total":total,"date":date})
    payment_id = result.fetchone()[0]
    print(payment_id)
    db.session.commit()
    for category in category_list:
        category_sql = "INSERT INTO paymentcategory (payment_id,category_id) VALUES (:payment_id,:category_id)"
        db.session.execute(category_sql, {"payment_id":payment_id,"category_id":int(category)})
    db.session.commit()
    return True
