from __future__ import absolute_import
from __future__ import unicode_literals

from flask import Blueprint
from flask import request

from api.decors import api

from .inputs import MakeBookingInputs
from .inputs import GetBookingsInputs

from models.function import post_booking_info
from models.function import get_booking_by_student
from models.function import get_booking_by_tutor

booking_blueprint = Blueprint("bookings", __name__, url_prefix="/bookings")


@booking_blueprint.route("/", methods=["POST"], strict_slashes=False)
@api(inputs_cls=MakeBookingInputs)
def make_booking():
    tutor_name = request.json.get("tutor_name")
    student_name = request.json.get("student_name")
    date = request.json.get("date")
    duration = request.json.get("duration")
    subject_id = request.json.get("subject_id")
    location = request.json.get("location")
    status = request.json.get("status")

    post_booking_info(tutor_name, student_name, date, duration, subject_id,
                      location, status)

    response = {
        "tutor_name": tutor_name,
        "student_name": student_name,
        "date": date,
        "duration": duration,
        "subject_id": subject_id,
        "location": location,
        "status": status
    }
    return response


@booking_blueprint.route("/<string:username>", methods=["GET"], strict_slashes=False)
@api(inputs_cls=GetBookingsInputs)
def get_bookings(username):
    is_student = request.json.get("is_student")

    if is_student is None or is_student:
        return get_booking_by_student(username)
    else:
        return get_booking_by_tutor(username)
