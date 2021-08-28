from __future__ import absolute_import
from __future__ import unicode_literals

from flask import Blueprint
from flask import jsonify

from api.decors import api

from models.function import get_profile

profile_blueprint = Blueprint("profile", __name__, url_prefix="/profile")


@profile_blueprint.route("/<string:username>", methods=["GET"])
@api()
def get_user_profile(username):
    return jsonify(get_profile(username))
