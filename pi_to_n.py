"""
Heres your docstring pylint >:(
    get_input

"""
import math

def get_input():
    """
    Gets an input
    """
    while True:
        try:
            index = int(raw_input("How many digits of PI do you want to print?"))
        except ValueError:
            print "Sorry, that was not a valid number..."
            continue
        else:
            if index <= 50:
                break
            else:
                print "Please enter a digit less than 50."
                continue
    return int(index)

def get_pi_to_digit(i):
    """
    Returns Pi to specified index
    """
    return '{:.{prec}f}'.format(math.pi, prec=i)

def print_result(response):
    """
    Prints the result
    """
    formatted_response = ("The precision of PI you asked for is %s!" % response)
    print formatted_response

print_result(get_pi_to_digit(get_input()))
print "\n"
