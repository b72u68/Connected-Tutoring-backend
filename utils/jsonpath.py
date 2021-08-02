from __future__ import absolute_import
from __future__ import unicode_literals


def get_value(d, path, default_value=None):
    """ Simple json path util function

    Enable get_value(d, "hits.hits.total") instead of
    d["hits"]["hits"]["total"]
    """
    try:
        elem = d
        for x in path.split("."):
            if str(x).isnumeric() and isinstance(elem, list):
                elem = elem[int(x)]
            else:
                elem = elem.get(x)
        return elem
    except:  # noqa
        return default_value


def get_cascading_value(d, paths, default_value=None):
    """
    Call the paths, return the first non-null result.
    """
    for path in paths:
        res = get_value(d, path)
        if res is not None:
            return res
    return default_value


def get_values(d, paths):
    result = []
    for path in paths:
        res = get_value(d, path)
        if res is not None:
            result.append(res)
    return result


def flatten(y):
    out = {}

    def _flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                _flatten(x[a], name + a + '.')
        elif type(x) is list:
            i = 0
            for a in x:
                _flatten(a, name + str(i) + '.')
                i += 1
        else:
            out[name[:-1]] = x

    _flatten(y)
    return out
