from six import add_metaclass, integer_types


class IntMeta(type):

    def __instancecheck__(self, other):
        try:
            for int_type in integer_types:
                int_type(other)
                return True
        except:
            return False


@add_metaclass(IntMeta)
class ExtentInt(object):
    pass
