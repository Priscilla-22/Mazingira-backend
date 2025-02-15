from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS

from models import db

app = Flask(__name__)

# Initialize CORS
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mazingira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

@app.route('/')
def index():
    return '<h1>Welcome To Mazingira</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
