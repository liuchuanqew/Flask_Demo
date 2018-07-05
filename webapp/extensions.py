from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_restful import Api
from flask_principal import Principal, Permission, RoleNeed


bcrypt = Bcrypt()
principals = Principal()
rest_api = Api()

admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))


login_manager = LoginManager()
login_manager.login_view = "main.login"
login_manager.session_protection = 'strong'
login_manager.login_message = "Please login to access this page"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(userid):
    from webapp.models import User
    return User.query.get(userid)
