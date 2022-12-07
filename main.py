import math
import sys
import time
import random


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


def sortArray(array: list, reverse: bool = False):
    """This function can be used to sort small arrays (recommended size lower than 20).\n\n

    array: The array that should get sorted\n
    reversed = False -> sorts the array from highest to lowest\n
    reversed = True -> sorts the array from lowest to highest"""
    if type(array) != list:
        raise TypeError(f"argument \"array\" must be an array, but you entered {type(array)}")
    if type(reverse) != bool:
        raise TypeError(f"argument \"reverse\" must be an bool, but you entered {type(array)}")

    def sort(index=0):
        while True:
            if index >= len(array) - 1:
                return array
            if array[index] >= array[index + 1]:
                index += 1
                continue
            else:
                array[index], array[index + 1] = array[index + 1], array[index]
                index = 0

    def sort_reverse(index=0):
        while True:
            if index >= len(array) - 1:
                return array
            if array[index] <= array[index + 1]:
                index += 1
                continue
            else:
                array[index], array[index + 1] = array[index + 1], array[index]
                index = 0

    if reverse:
        sort_reverse()
    else:
        sort()
    return array


def shuffle(array: list):
    """This function can be used to shuffle  arrays).\n\n

        array: The array that should get shuffled"""
    if type(array) != list:
        raise TypeError(f"argument \"array\" must be an array, but you entered {type(array)}")

    for _ in range(len(array)):
        idx1 = random.randint(0, len(array) - 1)
        idx2 = random.randint(0, len(array) - 1)

        array[idx1], array[idx2] = array[idx2], array[idx1]
    return array


def compare_floats(float1: float, float2: float, tolerance: int = 1e-10, return_bool: bool = True):
    """This function is used to check if two floats are within the specified range. Default range: 1e-10 \n
    There are two modes:

    return_bool = True -> Return True or False (default) \n
    return_bool = False -> Returns the two numbers if the check is True
    """
    if type(float1) or type(float2) != float:
        raise TypeError(
            f"arguments \"float1\" and \"float2\" must be a float, but you entered {type(float1)} and {type(float2)}")
    if type(tolerance) != int:
        raise TypeError(f"argument \"tolerance\" must be an int, but you entered {type(float1)} and {type(float2)}")
    if type(return_bool) != bool:
        raise TypeError(f"argument \"return_bool\" must be a bool, but you entered {type(float1)} and {type(float2)}")

    absolute = abs(float1 - float2)
    if return_bool:
        return absolute <= tolerance
    elif not return_bool and absolute <= tolerance:
        return float1, float2


def toString(arr: list):
    """This function can be used to convert arrays/tuples to a string.\n\n

    toString(arr):\n
    arr: is the iterable to be converted to a string"""
    if type(array) != list:
        raise TypeError(f"argument \"array\" must be an array, but you entered {type(array)}")

    data = ""
    for i in arr:
        data += str(i)
    return data


if __name__ == '__main__':  # test area
    pass
