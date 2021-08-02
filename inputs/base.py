import logging
from copy import deepcopy

from jsonschema import FormatChecker
from jsonschema.exceptions import ValidationError
from six import iteritems

from utils import jsonpath

from .schema import validate

logger = logging.getLogger(__name__)


class Inputs(object):

    validate_operator = 'and'

    def __init__(self):
        self._parts = {}

    @staticmethod
    def _handle_custom_message(err, schema):
        if not isinstance(err, ValidationError):
            return

        absolute_schema_path = deepcopy(err.absolute_schema_path)
        if absolute_schema_path and len(absolute_schema_path) > 1:
            attr_error = absolute_schema_path.pop()
            full_path = '.'.join(absolute_schema_path)
            message_path = "%s.message" % full_path
            message = jsonpath.get_value(schema, message_path) or {}
            if message.get(attr_error):
                err.message = message[attr_error]

    def validate(self):
        last_exception = None
        for name, value in iteritems(self._parts):
            schema = getattr(self, name, None)
            if schema:
                try:
                    validate(value, schema, format_checker=FormatChecker())
                    if self.validate_operator == 'or':
                        return
                except Exception as e:
                    # TODO: narrow exception type
                    e.part = name
                    self._handle_custom_message(e, schema)
                    if self.validate_operator == 'and':
                        raise
                    last_exception = e

        if self.validate_operator == 'or' and last_exception:
            raise last_exception
