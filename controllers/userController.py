from flask import jsonify, request, Blueprint, session
from services.userService import create_user, update_user, delete_user, get_by_id
from models.user import User
from data.responses.loginResponse import LoginResponse
bp = Blueprint('user', __name__)

# =========================== ROTAS ===========================
@bp.route('/register', methods=['POST'])
def add_user():
    data = request.json
    new_user = create_user(data['fullname'], data['password'], data['email'], data['birth'])
    return jsonify({'message': new_user.to_json()})

@bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(id):
    if request.method == 'PUT':
        return update_user_controller(id)
    elif request.method == 'DELETE':
        return delete_user_controller(id)
    elif request.method == 'GET':
        return get_user_by_id_controller(id)

@bp.route('/login', methods=['POST'])
def login():
    return login_controller()

@bp.route('/getAll', methods=['GET'])
def get_all():
    users = get_all_users()
    return jsonify({'users': [user.to_json() for user in users]})
# =========================== ROTAS ===========================




# ======================== FUNCOES ============================

def update_user_controller(id):
    data = request.json
    updated_user = update_user(id, data.get('fullname'), data.get('password'), data.get('email'))
    if not updated_user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'updated_user': updated_user.to_json()})

def delete_user_controller(id):
    deleted_user = delete_user(id)
    if not deleted_user:
        return jsonify({'message': 'User not found'}), 404
    return jsonify({'deleted_user': f'User {id} deleted'})

def get_user_by_id_controller(id):
    user = get_by_id(id)
    if not user:
        return jsonify({'message': 'User not found'}), 404
    
    return jsonify({'GetUserByID': user.to_json()})

def login_controller():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and user.password == data['password']:
        user_session = LoginResponse(user.id, user.fullname)
        session['cookie'] = user.id
        session['user'] = user_session.to_json()
    
        
        return jsonify({'message': f'Logged in successfully, session: {session["cookie"]}', 'obj': user_session.to_json()})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401
    
def get_all_users():
    return User.query.all()

# ======================== FUNCOES ============================