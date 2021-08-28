from __future__ import absolute_import
from __future__ import unicode_literals

from flask import Blueprint
from flask import request

from api.decors import api

from .inputs import SearchClassesInputs

from models.function import get_live_classes
from models.function import get_open_classes
from models.function import get_classes_by_user

class_blueprint = Blueprint("classes", __name__, url_prefix="/classes")


@class_blueprint.route("/", methods=["GET"], strict_slashes=False)
@api(inputs_cls=SearchClassesInputs)
def search_classes():
    is_live = request.args.get("is_live")

    if not is_live:
        return get_open_classes()
    else:
        return get_live_classes()


@class_blueprint.route("/<string:username>", methods=["GET"])
@api()
def get_personal_classes(username):
    return get_classes_by_user(username)
