from __future__ import absolute_import
from __future__ import unicode_literals

from inputs import FlaskInputs


class SearchTutorsInputs(FlaskInputs):
    params = {
        "type": "object",
        "properties": {
            "subject": {
                "type": "string"
            },
            "location": {
                "type": "string"
            },
            "rating": {
                "type": "number",
            },
            "is_active": {
                "type": "boolean"
            },
            "first_name": {
                "type": "string"
            },
            "last_name": {
                "type": "string"
            }
        }
    }
