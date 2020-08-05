from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from ISAQ.config import Config

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'admin_b.login'

def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    
    bcrypt.init_app(app)
    login_manager.init_app(app)
    db.init_app(app)

    from ISAQ.admin.routes import admin_b
    from ISAQ.main.routes import main_b

    app.register_blueprint(admin_b)
    app.register_blueprint(main_b)

    return app