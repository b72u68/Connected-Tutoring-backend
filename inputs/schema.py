from __future__ import absolute_import
from __future__ import unicode_literals

from jsonschema.validators import Draft3Validator
from jsonschema.validators import Draft4Validator
from jsonschema import validate as _validate

from .types import ExtentInt
from .validators import minimum
from .validators import maximum

Draft4Validator.VALIDATORS['minimum'] = minimum
Draft4Validator.VALIDATORS['maximum'] = maximum
Draft3Validator.VALIDATORS['minimum'] = minimum
Draft3Validator.VALIDATORS['maximum'] = maximum


def validate(instance, schema, cls=None, *args, **kwargs):
    kwargs['types'] = {'integer': ExtentInt}
    _validate(instance, schema, cls, *args, **kwargs)
