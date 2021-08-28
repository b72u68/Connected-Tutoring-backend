from __future__ import absolute_import
from __future__ import unicode_literals

from functools import wraps

from flask import jsonify
from flask import Response


def api(inputs_cls=None,
        success_code=200):

    def _decor(f):

        @wraps(f)
        def _wrap(*args, **kwargs):
            try:
                # Validate inputs
                if inputs_cls:
                    inputs = inputs_cls()
                    inputs.validate()

                # Make response
                response = f(*args, **kwargs)
                if isinstance(response, (Response, str, str)):
                    return response
                else:
                    res = jsonify(response)
                    res.status_code = success_code

                    return res

            except Exception as e:
                return {
                    'message': e,
                    'error': True,
                }
        return _wrap

    return _decor
