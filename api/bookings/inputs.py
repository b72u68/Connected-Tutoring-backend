from __future__ import absolute_import
from __future__ import unicode_literals

from inputs import FlaskInputs


class MakeBookingInputs(FlaskInputs):
    json = {
        "type": "object",
        "properties": {
            "tutor_name": {
                "type": "string"
            },
            "student_name": {
                "type": "string"
            },
            "date": {
                "type": "string",
                "format": "date"
            },
            "duration": {
                "type": "number"
            },
            "subject_id": {
                "type": "number"
            },
            "location": {
                "type": "string"
            },
            "status": {
                "type": "string"
            },
        },
        "required": [
            "tutor_name", "student_name", "date", "duration", "subject_id",
            "location"]
    }


class GetBookingsInputs(FlaskInputs):
    json = {
        "type": "object",
        "properties": {
            "q": {
                "type": "string"
            },
            "subject": {
                "type": "string"
            },
            "date": {
                "type": "string",
                "format": "date"
            },
            "is_student": {
                "type": "boolean"
            },
        },
        "required": ["is_student"]
    }
