from __future__ import absolute_import
from __future__ import unicode_literals

from inputs import FlaskInputs


class GetBookingsInputs(FlaskInputs):
    params = {
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
            }
        }
    }
