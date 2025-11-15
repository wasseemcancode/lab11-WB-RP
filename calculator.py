# https://github.com/wasseemcancode/lab11-WB-RP 
import math 
def square_root(a): 
    if a < 0: 
        raise ValueError 
    else: return math.sqrt(a) 

def hypotenuse(a, b): 
    if a < 0 or b < 0: 
        raise ValueError("Sides must be non-negative.") 
    return math.hypot(a, b) 
def add(a, b): 
    return a+ b 
def subtract(a, b): 
    return a - b 
def mul(a,b): return a*b 
def div(a,b): 
    if a == 0: 
        raise ZeroDivisionError 
    else: 
        return b / a 
def logarithm(a,b): 
    if a == 0: raise ValueError 
    elif b == 0 or b == 1: 
        raise ValueError 
    else: 
        return math.log(a,b) 
def exp(a,b): 
    return a**b 