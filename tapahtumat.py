from db import db
import users

# Tapahtumia koskevat SQL:t
def laske_tapahtumat():
    result = db.session.execute("SELECT COUNT(*) FROM tapahtumat")
    counter = result.fetchone()[0]
    return counter

def listaa_tapahtumat():
    result = db.session.execute("SELECT id, nimi FROM tapahtumat ORDER BY id DESC")
    tapahtumalista = result.fetchall()
    return tapahtumalista

def lisaa_tapahtuma(nimi):
    user_id = users.user_id()
    sql = "INSERT INTO tapahtumat (nimi, kayttaja) VALUES (:nimi,:user_id)"
    db.session.execute(sql, {"nimi":nimi,"user_id":user_id})
    db.session.commit()
    return True

def hae_tapahtuma(id):
    sql = "SELECT id, nimi, kayttaja FROM tapahtumat WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    tapahtumatiedot = result.fetchall()
    return tapahtumatiedot
