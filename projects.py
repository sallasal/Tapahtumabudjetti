from db import db
import users

# Tapahtumia koskevat SQL:t
def count_projects():
    result = db.session.execute("SELECT COUNT(*) FROM tapahtumat")
    counter = result.fetchone()[0]
    return counter

def list_projects():
    result = db.session.execute("SELECT id, nimi FROM tapahtumat ORDER BY id DESC")
    tapahtumalista = result.fetchall()
    return tapahtumalista

def add_project(nimi):
    user_id = users.user_id()
    sql = "INSERT INTO tapahtumat (nimi, kayttaja) VALUES (:nimi,:user_id)"
    db.session.execute(sql, {"nimi":nimi,"user_id":user_id})
    db.session.commit()
    return True

def get_project(id):
    sql = "SELECT id, nimi, kayttaja FROM tapahtumat WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    tapahtumatiedot = result.fetchone()
    return tapahtumatiedot
