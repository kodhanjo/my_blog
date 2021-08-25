from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

# Initializing application
bootstrap = Bootstrap()

def create_app(config_name):

    app = Flask(__name__)

#initialize flask extensions
    bootstrap.init_app(app)
# Setting up configuration
    app.config.from_object(config_options[config_name])
# register_blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app


# from flask import Flask
# from flask_bootstrap import Bootstrap
# from config import config_options, DevConfig
# # from flask_sqlalchemy import SQLAlchemy
# # from flask_login import LoginManager
# # from flask_mail import Mail
# # from flask_uploads import UploadSet,configure_uploads,IMAGES

# bootstrap = Bootstrap()
# # db = SQLAlchemy()
# # mail = Mail()
# # photos = UploadSet('photos',IMAGES)

# # login_manager = LoginManager()
# # login_manager.session_protection = 'strong'
# # login_manager.login_view = 'auth.login'

# def create_app(config_name):

#     app = Flask(__name__)

#     # Creating the app configurations
#     app.config.from_object(config_options[config_name])

#     # Initializing flask extensions
#     bootstrap.init_app(app)
#     # db.init_app(app)
#     login_manager.init_app(app)
#     mail.init_app(app)

#     # configure UploadSet
#     # configure_uploads(app,photos)

#     #registering blueprint
#     from .main import main as main_blueprint
#     app.register_blueprint(main_blueprint)

#     from .auth import auth as auth_blueprint
#     app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

#     return app
