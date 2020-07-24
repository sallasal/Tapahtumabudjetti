from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

def login(username,password):
    sql = "SELECT salasana, id FROM kayttajat WHERE nimi=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["user_id"] = user[1]
            return True
        else:
            return False

def logout():
    del session["user_id"]

def register(username,password,email):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO kayttajat (nimi,salasana,email) VALUES (:username,:password,:email)"
        db.session.execute(sql, {"username":username,"password":hash_value,"email":email})
        db.session.commit()
    except:
        return False
    return login(username,password)

def user_id():
    return session.get("user_id",0)
