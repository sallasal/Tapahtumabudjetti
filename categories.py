from db import db

def add_category(name,project_id):
    sql = "INSERT INTO categories (name,project_id) VALUES (:name,:project_id)"
    db.session.execute(sql, {"name":name,"project_id":project_id})
    db.session.commit()
    return True

def list_categories(project_id):
    sql = "SELECT id, name FROM categories WHERE project_id=:project_id ORDER BY id ASC"
    result = db.session.execute(sql, {"project_id":project_id})
    category_list = result.fetchall()
    return category_list
