from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash

# Check credentials and if accepted, start new session
def login(username,password):
    sql = "SELECT password, id FROM users WHERE name=:username"
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

# End user session
def logout():
    del session["user_id"]

# Register new user to db
def register(username,password,email):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (name,password,email) VALUES (:username,:password,:email)"
        db.session.execute(sql, {"username":username,"password":hash_value,"email":email})
        db.session.commit()
    except:
        return False
    return login(username,password)

# Get user id from current session
def user_id():
    return session.get("user_id",0)

# Get user name and email for defined user id
def user_name(id):
    sql = "SELECT name, email FROM users WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    user_information = result.fetchone()
    return user_information
