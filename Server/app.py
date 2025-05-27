from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Configure your database (example: SQLite)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions with app
    db.init_app(app)
    migrate.init_app(app, db)

    # Set up Flask-RESTful
    api = Api(app)

    # Register your resources
    from resources.hello import Hello
    api.add_resource(Hello, '/')

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
