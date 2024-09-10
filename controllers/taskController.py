from flask import Blueprint, request, jsonify, session
from models.task import Task
from services.taskService import create_task,delete_task, update_task, update_status_id, get_task_bygroup

bp = Blueprint('task', __name__)

@bp.route('/create', methods=['POST'])
def create():
    data = request.json
    task = create_task(data['title'], data['desc'], session['cookie'], data['group_id'])
    return jsonify({'Message': task.to_json()})

@bp.route('/delete', methods=['DELETE'])
def delete():
    data = request.json
    return jsonify({'Message': f'{delete_task(data['task_id'], session['cookie'])}'})

@bp.route('/update', methods=['PUT'])
def update():
    data = request.json
    update_task(data['task_id'], data['title'], data['desc'])
    return jsonify({'Message': f'Updated task {data["task_id"]}'})

@bp.route('/group', methods=['GET'])
def get():
    group_id = request.args.get('id', type=int)
    tasks = get_task_bygroup(group_id)
    return jsonify({'group_tasks': [task for task in tasks]})


