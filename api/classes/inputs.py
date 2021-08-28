from __future__ import absolute_import
from __future__ import unicode_literals

from inputs import FlaskInputs


class SearchClassesInputs(FlaskInputs):
    params = {
        "type": "object",
        "properties": {
            "is_live": {
                "type": "boolean"
            }
        }
    }
