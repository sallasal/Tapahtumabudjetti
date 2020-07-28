from db import db

# Osaprojekteja koskevat SQL:t
def list_all_subprojects():
    result = db.session.execute("SELECT id, nimi, budjettisumma FROM osaprojektit ORDER BY id DESC")
    osaprojektilista = result.fetchall()
    return osaprojektilista

def add_subproject(name,total_sum,project_id):
    sql = "INSERT INTO osaprojektit (nimi, budjettisumma,tapahtuma) VALUES (:name,:total_sum,:project_id)"
    db.session.execute(sql, {"name":name,"total_sum":total_sum,"project_id":project_id})
    db.session.commit()
    return True

