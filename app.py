from flask import Flask
from routes.authRoutes import auth
from routes.userRoutes import user

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(user)

if __name__ == '__main__':
    app.run()
