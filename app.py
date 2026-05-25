from flask import Flask
from flask_cors import CORS
from routes.viewRoute import view
from routes.apiRoute import api

app = Flask(__name__)

CORS(app)

app.register_blueprint(view)
app.register_blueprint(api)

if __name__ == '__main__':
    app.run()
