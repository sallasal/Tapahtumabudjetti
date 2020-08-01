from db import db

def add_category(name,project_id):
    sql = "INSERT INTO categories (name,project_id) VALUES (:name,:project_id)"
    db.session.execute(sql, {"name":name,"project_id":project_id})
    db.session.commit()
    return True

