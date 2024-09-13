from flask import Blueprint, request, jsonify, session
from models.group import Group
from models.userGroup import UserGroup
from services.userGroupService import invite_user, get_user_groups
from services.groupService import create_group, verify_admin, define_group


bp = Blueprint('group', __name__)
bp1 = Blueprint('userGroup', __name__)

# =========================== ROTAS ===========================
@bp.route('/create', methods=['POST'])
def create():
    data = request.json
    group = create_group(data['name'], data['admin_id'])
    if not group:
        return jsonify({'message': 'Create failed'}), 404
    return jsonify({'group': group.to_json()})

@bp.route('/invite', methods=['POST'])
def invite():
    data = request.json
    if verify_admin(data['group_id'], data['curr_user_id']):
        user_invited = invite_user(data['user_id'], data['group_id'])
        if not user_invited:
            return jsonify({'message': 'Invite failed'}), 404
        return jsonify({'user_invited': user_invited.to_json()})
    else:
        return jsonify({'message': f'You are not admin in group {data["group_id"]}'}), 403


@bp.route('/get/user', methods=['GET'])
def get_groups():
    user_id = request.args.get('id', type=int)
    user_groups = get_user_groups(user_id)
    return jsonify({'user_groups': [group for group in user_groups]})

@bp.route('/define', methods=['POST'])
def define():
    data = request.json
    define_group(data['group_id'])
    return jsonify({'message': f'Group {data['group_id']} defined'})