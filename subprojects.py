from db import db

# Get full subproject information list, including total sum, for project page
def list_subprojects(project_id):
    sql = """SELECT s.id, s.name, s.total, SUM(p.total) FROM payments p 
        RIGHT JOIN subprojects s ON p.subproject=s.id 
        WHERE s.project=:project_id GROUP BY s.id, s.name, s.total"""
    result = db.session.execute(sql, {"project_id":project_id})
    subproject_list = result.fetchall()
    final_list = []
    for row in subproject_list:
        rowlist = list(row)
        if rowlist[3] == None:
            rowlist[3] = 0
        difference = rowlist[2] - rowlist[3]
        rowlist.append(difference)
        final_list.append(tuple(rowlist))
    return final_list

# Add new subproject to database
def add_subproject(name,total_sum,project_id):
    sql = "INSERT INTO subprojects (name,total,project) VALUES (:name,:total_sum,:project_id)"
    db.session.execute(sql, {"name":name,"total_sum":total_sum,"project_id":project_id})
    db.session.commit()
    return True

# Update budgeted sum for one subproject
def update_total(subproject_id,newtotal):
    sql = "UPDATE subprojects SET total=:newtotal WHERE id=:subproject_id"
    db.session.execute(sql, {"newtotal":newtotal,"subproject_id":subproject_id})
    db.session.commit()
    return True

# Get subproject total sum for any project
def get_grandtotal(project_id):
    sql = "SELECT SUM(total) FROM subprojects WHERE project=:project_id"
    result = db.session.execute(sql, {"project_id":project_id})
    grandtotal = result.fetchone()[0]
    return grandtotal

#List all payments from subproject
def payments_in_subproject(subproject_id):
    sql = """SELECT p.recipient, p.message, p.total, p.date, users.name FROM payments p 
        LEFT JOIN users ON users.id=p.userid 
        LEFT JOIN subprojects s ON s.id=p.subproject 
        WHERE p.subproject=:subproject_id"""
    result = db.session.execute(sql, {"subproject_id":subproject_id})
    subproject_payments = result.fetchall()
    return subproject_payments
