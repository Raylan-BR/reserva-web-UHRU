from flask import Flask
from flask_cors import CORS
from routes.authRoutes import auth
from routes.userRoutes import user
from routes.pageRoutes import page

app = Flask(__name__)

CORS(app)

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(page)

if __name__ == '__main__':
    app.run()
