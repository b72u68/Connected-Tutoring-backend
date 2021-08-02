from __future__ import absolute_import
from __future__ import unicode_literals

from functools import wraps

from flask import request as flask_request
from flask import jsonify
from flask import Response


def api(inputs_cls=None, request_cls=None,
        success_code=200):

    def _decor(f):

        @wraps(f)
        def _wrap(*args, **kwargs):
            try:
                # Validate inputs
                if inputs_cls:
                    inputs = inputs_cls()
                    inputs.validate()

                # Convert flask request to protobuf message
                if request_cls:
                    request = _get_request(request_cls)
                    args = (request, ) + args

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
                    'message': e.message,
                    'error': True,
                }
        return _wrap

    return _decor


def _get_request(request_cls, **kwargs):
    request = request_cls()
    body = flask_request.get_json(force=True, silent=True)
    if body:
        return request
