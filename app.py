from flask import Flask, render_template
from flask_cors import CORS
from config import Config
from helper import db
from controllers.userController import bp as user_bp
from controllers.groupController import bp as group_bp, bp1 as userGroup_bp
from controllers.statusController import bp as status_bp
from controllers.taskController import bp as task_bp


def create_bps(app):
    pass

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
    app.config.from_object(Config)
    db.init_app(app)
    create_bps(app)
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(group_bp, url_prefix='/group')
    app.register_blueprint(status_bp, url_prefix='/status')
    app.register_blueprint(task_bp, url_prefix='/task') 
    app.register_blueprint(userGroup_bp, url_prefix='/user_group')
    return app

if __name__ == '__main__': 
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
