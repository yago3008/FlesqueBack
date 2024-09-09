from models.task import Task
from models.userGroup import UserGroup
from helper import db

def create_task(title, desc, user_id, group_id):
    task = Task(title=title, desc=desc, user_id=user_id, group_id=group_id, status_id=1)
    db.session.add(task)
    db.session.commit()
    return task

def update_status_id(id, status_id):
    task = Task.query.get(id)
    if not task:
        return None
    
    if not status_id:
        return None
    task.status_id = status_id
    
    db.session.commit()
    return task

def update_task(id, title=None, desc=None):
    task = Task.query.get(id)
    if not task:
        return None
    
    if title:
        task.title = title
    if desc:
        task.desc = desc

    db.session.commit()
    return task

def verify_admin(task_id, admin_id):
    task = Task.query.filter_by(task_id=task_id).first()
    if task and task.user_id == admin_id:
        return True
    return False

def delete_task(id, admin_id):
    if not verify_admin(id, admin_id):
        return f"You do not have permission to delete this task"
    task = Task.query.get(id)
    if task:
        db.session.delete(task)
        db.session.commit()
        return f"Task {id} deleted successfully"

def get_task(group_id, user_id):
    tasks = Task.query.filter_by(group_id=group_id, user_id=user_id).all()
    return [task.id for task in tasks]


    




