from models.task import Task
from models.user import User
from models.group import Group
from helper import db
from flask import jsonify

def create_task(title, desc, user_name, group_id):
    user = User.query.filter_by(fullname=user_name).first()
    task = Task(title=title, desc=desc, user_id=user.id, group_id=group_id, status_id=1)
    db.session.add(task)
    db.session.commit()
    print("commited")
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

def delete_task(taskId, userId):
    task = Task.query.get(taskId)
    group = Group.query.get(task.group_id)

    if int(userId) != int(group.admin_id):
        return None

    print("LAMBADA")
    
    db.session.delete(task)
    db.session.commit()
    return task

def get_task(group_id, user_id):
    tasks = Task.query.filter_by(group_id=group_id, user_id=user_id).all()
    return [task.id for task in tasks]

def get_task_bygroup(group_id):
    tasks = Task.query.filter_by(group_id=group_id).join(User).add_entity(User).all()
    return [{ "task": task[0].to_json(), "user": task[1].to_json() } for task in tasks]

def get_task_by_id(task_id):
    return Task.query.get(task_id)
