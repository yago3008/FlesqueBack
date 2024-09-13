from flask import Blueprint, request, jsonify, session
from models.task import Task
from services.taskService import create_task,delete_task, update_task, update_status_id, get_task_bygroup, get_task_by_id

bp = Blueprint('task', __name__)

@bp.route('/create', methods=['POST'])
def create():
    data = request.json
    print(data)
    task = create_task(data['title'], data['desc'], data['user_name'], data['group_id'])
    print(task.title + task.desc)
    return jsonify({'Message': task.to_json()})

@bp.route('/delete', methods=['POST'])
def delete():
    data = request.json
    response = delete_task(data['task_id'], data['user_id'])
    if(response == None):
        return jsonify({'Message': 'Error deleting task'}), 403
    
    return jsonify({'Message': 'Success deleting taks'}), 200

@bp.route('/update', methods=['PUT'])
def update():
    data = request.json
    update_task(data['task_id'], data['title'], data['desc'])
    return jsonify({'Message': f'Updated task {data["task_id"]}'})

@bp.route('/group', methods=['GET'])
def get():
    group_id = request.args.get('id', type=int)
    filter = request.args.get('filter', type=str)
    tasks = get_task_bygroup(group_id, filter)
    return jsonify({'group_tasks': [task for task in tasks]})

@bp.route('/', methods=['GET'])
def getOne():
    task_id = request.args.get('id', type=int)
    task = get_task_by_id(task_id)
    print(task)
    return jsonify({'task': task.to_json()})
