from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

from models import db
# from flask_bcrypt import Bcrypt


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mazingira.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True  )


app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)
api = Api(app)
# bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return '<h1>Welcome To Mazingira</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)