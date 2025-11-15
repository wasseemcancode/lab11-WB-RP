# https://github.com/wasseemcancode/lab11-WB-RP

import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)


def hypotenuse(a, b):
    # Tests expect negative sides to be treated as magnitudes, not errors
    return math.hypot(abs(a), abs(b))


def add(a, b): 
    return a + b


def subtract(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError
    return a / b


def logarithm(a, b):
    # Tests expect: logarithm(base, argument) → log_base(argument)
    if a <= 0 or a == 1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(b, a)


def exp(a, b):
    return a ** b