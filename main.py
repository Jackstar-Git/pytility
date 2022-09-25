import math
import sys


class FixNumber:
    """This function is used to fix Pythons floating-point error."""
    EPSILON = sys.float_info.epsilon

    @classmethod
    def down(cls, n, x=10):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        next lowest number.\n\n

        near(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return math.floor((n + cls.EPSILON) * (10 ** x)) / (10 ** x)

    @classmethod
    def up(cls, n, x=10):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        next highest number.\n\n

        up(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return math.ceil((n + cls.EPSILON) * (10 ** x)) / (10 ** x)

    @classmethod
    def near(cls, n, x=10):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        nearest number.\n\n

        near(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return round((n + cls.EPSILON) * (10 ** x)) / (10 ** x)


def toString(arr):
    """This function can be used to convert arrays/tuples to a string.\n\n

    toString(arr):\n
    arr: is the iterable to be converted to a string"""
    data = ""
    for i in arr:
        data += str(i)
    return data
