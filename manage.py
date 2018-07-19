from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig

#  init a flask application
app = Flask(__name__)

#  load flask config from config.py
app.config.from_object(DevConfig)

#  init flask_sqlalchemy
db = SQLAlchemy(app)

# init flask_manager
manager = Manager(app)

# init flask_migrate
migrate = Migrate(app, db)

# add development server startup command
manager.add_command('runserver', Server())
# set db is manage models (flask_migrate)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db)


if __name__ == '__main__':
    manager.run()
