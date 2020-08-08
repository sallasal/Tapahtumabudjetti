from db import db
import users

# Count all projects for index page
def count_projects():
    result = db.session.execute("SELECT COUNT(*) FROM projects")
    counter = result.fetchone()[0]
    return counter

#List all projects
def list_projects():
    result = db.session.execute("SELECT id, name FROM projects ORDER BY name ASC")
    project_list = result.fetchall()
    return project_list

#List projects for user logged in
def list_user_projects(user_id):
    sql = "SELECT id, name FROM projects WHERE userid=:user_id ORDER BY name"
    result = db.session.execute(sql, {"user_id":user_id})
    user_project_list = result.fetchall()
    return user_project_list

# List all other projects than those ones that have logged-in user as owner
def list_other_projects(user_id):
    sql = "SELECT id, name FROM projects WHERE NOT userid=:user_id ORDER BY name"
    result = db.session.execute(sql, {"user_id":user_id})
    other_projects_list = result.fetchall()
    return other_projects_list

# Add new project to system
def add_project(name):
    user_id = users.user_id()
    sql = "INSERT INTO projects (name, userid) VALUES (:name,:user_id)"
    db.session.execute(sql, {"name":name,"user_id":user_id})
    db.session.commit()
    return True

# Get full project information for defined project
def get_project(id):
    sql = "SELECT id, name, userid FROM projects WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    project_information = result.fetchone()
    return project_information

# Get user information of defined project
def get_userid(id):
    sql = "SELECT userid FROM projects WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    userid = result.fetchone()
    return userid
