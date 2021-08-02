from flask import request

from .base import Inputs


class FlaskInputs(Inputs):

    def __init__(self):
        super(FlaskInputs, self).__init__()
        self._parts = {
            'params': dict(request.args.to_dict()),
            'headers': dict(request.headers),
            'cookies': dict(request.cookies),
            'json': request.get_json(force=True, silent=True),
            'values': dict(request.values),
            'form': dict(request.form),
            'rule': dict(request.view_args)
        }
