from db import db

# Osaprojekteja koskevat SQL:t
def listaa_kaikki_osaprojektit():
    result = db.session.execute("SELECT id, nimi, budjettisumma FROM osaprojektit ORDER BY id DESC")
    osaprojektilista = result.fetchall()
    return osaprojektilista

def lisaa_osaprojekti(nimi,budjettisumma,tapahtumaid):
    sql = "INSERT INTO osaprojektit (nimi, budjettisumma,tapahtuma) VALUES (:nimi,:budjettisumma,:tapahtumaid)"
    db.session.execute(sql, {"nimi":nimi,"budjettisumma":budjettisumma,"tapahtumaid":tapahtumaid})
    db.session.commit()
    return True

