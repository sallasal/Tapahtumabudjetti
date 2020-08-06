from db import db

# Osaprojekteja koskevat SQL:t
def list_subprojects(project_id):
    sql = "SELECT id, name, total FROM subprojects WHERE project=:project_id ORDER BY name ASC"
    result = db.session.execute(sql, {"project_id":project_id})
    subproject_list = result.fetchall()
    return subproject_list

def add_subproject(name,total_sum,project_id):
    sql = "INSERT INTO subprojects (name,total,project) VALUES (:name,:total_sum,:project_id)"
    db.session.execute(sql, {"name":name,"total_sum":total_sum,"project_id":project_id})
    db.session.commit()
    return True

def update_total(subproject_id,newtotal):
    sql = "UPDATE subprojects SET total=:newtotal WHERE id=:subproject_id"
    db.session.execute(sql, {"newtotal":newtotal,"subproject_id":subproject_id})
    db.session.commit()
    return True

def get_grandtotal(project_id):
    sql = "SELECT SUM(total) FROM subprojects WHERE project=:project_id"
    result = db.session.execute(sql, {"project_id":project_id})
    grandtotal = result.fetchone()[0]
    return grandtotal
