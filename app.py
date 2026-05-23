from flask import Flask
from flask_cors import CORS
from routes.authRoutes import auth
from routes.userRoutes import user

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
