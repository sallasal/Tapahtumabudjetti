from db import db

# Tapahtumia koskevat SQL:t
def laske_tapahtumat():
    result = db.session.execute("SELECT COUNT(*) FROM tapahtumat")
    counter = result.fetchone()[0]
    return counter
