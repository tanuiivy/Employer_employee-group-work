from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api

# Initialize exten
db = SQLAlchemy()
migrate = Migrate()

app = Flask(__name__)

    # Configure your database (example: SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

    # Initialize extensions with app
db.init_app(app)
migrate.init_app(app, db)

    # Set up Flask-RESTful
api = Api(app)

class Home(Resource):
    def get(self):
        response_dict={
            "message":"Welcome to Employee record"
        }
        response = make_response(
            response_dict,
            200,)
        return response
api.add_resource(Home, '/')  
    


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
