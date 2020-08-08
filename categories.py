from db import db

# Add new category for defined project
def add_category(name,project_id):
    sql = "INSERT INTO categories (name,project_id) VALUES (:name,:project_id)"
    db.session.execute(sql, {"name":name,"project_id":project_id})
    db.session.commit()
    return True

# List all categories with defined project
def list_categories(project_id):
    sql = "SELECT id, name FROM categories WHERE project_id=:project_id ORDER BY id ASC"
    result = db.session.execute(sql, {"project_id":project_id})
    category_list = result.fetchall()
    return category_list

# List all payments in defined category
def payments_in_category(category_id):
    sql = "SELECT p.recipient,p.message,p.total,p.date FROM payments p, categories c, paymentcategory q WHERE q.payment_id=p.id AND q.category_id=c.id AND category_id=:category_id"
    result = db.session.execute(sql, {"category_id":category_id})
    payments_in_category = result.fetchall()
    return payments_in_category
