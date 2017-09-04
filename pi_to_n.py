"""
Heres your docstring pylint >:(
"""
import math

def get_input():
    print 'How many digits after the decimal would you like to print Pi?'
    index = raw_input()
    return int(index)

def get_pi_to_digit(i):
    return round(math.pi, i)

def print_result(res):
    s = ("The precision of PI you asked for is %f!" % res)
    print s

print_result(get_pi_to_digit(get_input()))
print "\n"