from db import db

# Osaprojekteja koskevat SQL:t
def list_all_subprojects():
    result = db.session.execute("SELECT id, nimi, budjettisumma FROM osaprojektit ORDER BY id DESC")
    osaprojektilista = result.fetchall()
    return osaprojektilista

def add_subproject(nimi,budjettisumma,tapahtumaid):
    sql = "INSERT INTO osaprojektit (nimi, budjettisumma,tapahtuma) VALUES (:nimi,:budjettisumma,:tapahtumaid)"
    db.session.execute(sql, {"nimi":nimi,"budjettisumma":budjettisumma,"tapahtumaid":tapahtumaid})
    db.session.commit()
    return True

