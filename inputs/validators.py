from jsonschema import _validators


def _to_number(value):
    try:
        return int(value)
    except ValueError:
        return float(value)


def minimum(validator, minimum, instance, schema):
    if validator.is_type(instance, "string"):
        try:
            instance = _to_number(instance)
        except Exception as e:
            pass

    for err in _validators.minimum(validator, minimum, instance, schema):
        yield err


def maximum(validator, maximum, instance, schema):
    if validator.is_type(instance, "string"):
        try:
            instance = _to_number(instance)
        except Exception as e:
            pass

    for err in _validators.maximum(validator, maximum, instance, schema):
        yield err
