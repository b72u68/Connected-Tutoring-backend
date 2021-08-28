from flask import Flask

from api import booking_blueprint
from api import profile_blueprint
from api import class_blueprint
from api import tutor_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(booking_blueprint)
    app.register_blueprint(profile_blueprint)
    app.register_blueprint(class_blueprint)
    app.register_blueprint(tutor_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
