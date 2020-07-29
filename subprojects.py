from db import db

# Osaprojekteja koskevat SQL:t
def list_subprojects():
    result = db.session.execute("SELECT id, name, total FROM subprojects")
    subproject_list = result.fetchall()
    return subproject_list

def add_subproject(name,total_sum,project_id):
    sql = "INSERT INTO subprojects (name,total,project) VALUES (:name,:total_sum,:project_id)"
    db.session.execute(sql, {"name":name,"total_sum":total_sum,"project_id":project_id})
    db.session.commit()
    return True

