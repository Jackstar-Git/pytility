import math
import sys
import time

class FixNumber:
    """This function is used to fix Pythons floating-point error."""
    EPSILON = sys.float_info.epsilon

    @classmethod
    def down(cls, number, round_to=10):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        next lowest number.\n\n

        near(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return round(math.floor((number + cls.EPSILON) * (10 ** round_to)) / (10 ** round_to), round_to)

    @classmethod
    def up(cls, number, round_to=100):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        next highest number.\n\n

        up(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return round(math.ceil((number + cls.EPSILON) * (10 ** round_to)) / (10 ** round_to), round_to)

    @classmethod
    def near(cls, number, round_to=10):
        """This function is used to fix Pythons floating-point error. The fixed number gets rounded to the
        nearest number.\n\n

        near(x, y) takes two arguments:\n
        x: is the number to be fixed\n
        y: represents the amount of digits to show after the decimal point. Default: 10"""
        return round((number + cls.EPSILON) * (10 ** round_to)) / (10 ** round_to)


def compare_floats(float1, float2, *, tolerance=1e-10, return_bool=True):
    """This function is used to check if two floats are within the specified range. Default range: 1e-10 \n
    There are two modes:

    return_bool = True -> Return True or False (default) \n
    return_bool = False -> Returns the two numbers if the check is True
    """
    absolute = abs(float1 - float2)
    if return_bool:
        return absolute <= tolerance
    elif not return_bool and absolute <= tolerance:
        return float1, float2


def toString(arr):
    """This function can be used to convert arrays/tuples to a string.\n\n

    toString(arr):\n
    arr: is the iterable to be converted to a string"""
    data = ""
    for i in arr:
        data += str(i)
    return data


if __name__ == '__main__':
    print(compare_floats(2, 4, tolerance=2))
