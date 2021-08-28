from __future__ import absolute_import
from __future__ import unicode_literals

from flask import Blueprint
from flask import request
from flask import jsonify

from api.decors import api

from .inputs import SearchTutorsInputs

from models.function import get_tutors_by_subject
from models.function import get_tutors_by_location
from models.function import get_tutors_by_rating
from models.function import get_tutors_by_active_status
from models.function import get_tutors_by_first_name
from models.function import get_tutors_by_last_name
from models.function import get_tutor_by_user

tutor_blueprint = Blueprint("tutors", __name__, url_prefix="/tutors")


@tutor_blueprint.route("/", methods=["GET"], strict_slashes=False)
@api(inputs_cls=SearchTutorsInputs)
def search_tutors():
    subject = request.args.get("subject")
    location = request.args.get("location")
    rating = request.args.get("rating")
    is_active = request.args.get("is_active")
    first_name = request.args.get("first_name")
    last_name = request.args.get("last_name")

    if subject:
        return jsonify(get_tutors_by_subject(subject))

    if location:
        return jsonify(get_tutors_by_location(location))

    if rating:
        return jsonify(get_tutors_by_rating(rating))

    if is_active:
        return jsonify(get_tutors_by_active_status(is_active))

    if first_name:
        return jsonify(get_tutors_by_first_name(first_name))

    if last_name:
        return jsonify(get_tutors_by_last_name(last_name))

    return {}


@tutor_blueprint.route("/<string:username>", methods=["GET"], strict_slashes=False)
@api()
def get_tutor_profile(username):
    return get_tutor_by_user(username)
