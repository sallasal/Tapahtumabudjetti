from db import db
import users

# Tapahtumia koskevat SQL:t
def count_projects():
    result = db.session.execute("SELECT COUNT(*) FROM projects")
    counter = result.fetchone()[0]
    return counter

def list_projects():
    result = db.session.execute("SELECT id, name FROM projects ORDER BY name ASC")
    project_list = result.fetchall()
    return project_list

def list_user_projects(user_id):
    sql = "SELECT id, name FROM projects WHERE userid=:user_id ORDER BY name"
    result = db.session.execute(sql, {"user_id":user_id})
    user_project_list = result.fetchall()
    return user_project_list

def list_other_projects(user_id):
    sql = "SELECT id, name FROM projects WHERE NOT userid=:user_id ORDER BY name"
    result = db.session.execute(sql, {"user_id":user_id})
    other_projects_list = result.fetchall()
    return other_projects_list

def add_project(name):
    user_id = users.user_id()
    sql = "INSERT INTO projects (name, userid) VALUES (:name,:user_id)"
    db.session.execute(sql, {"name":name,"user_id":user_id})
    db.session.commit()
    return True

def get_project(id):
    sql = "SELECT id, name, userid FROM projects WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    project_information = result.fetchone()
    return project_information

def get_userid(id):
    sql = "SELECT userid FROM projects WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    userid = result.fetchone()
    return userid
