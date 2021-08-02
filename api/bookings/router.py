from __future__ import absolute_import
from __future__ import unicode_literals

from flask import Blueprint
from flask import request

from api.decors import api

from .inputs import GetBookingsInputs

booking_blueprint = Blueprint("bookings", __name__, url_prefix="/bookings")


@booking_blueprint.route("/", methods=["POST"], strict_slashes=False)
def make_booking():
    return "Hello POST"


@booking_blueprint.route("/", methods=["GET"], strict_slashes=False)
@api(inputs_cls=GetBookingsInputs)
def get_bookings():
    return "Hello GET"
