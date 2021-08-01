from flask import Flask

from api import booking_blueprint


def create_app():
    app = Flask(__name__)

    app.register_blueprint(booking_blueprint)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
