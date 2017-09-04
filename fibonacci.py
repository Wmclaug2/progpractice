"""
Returns the fibonacci sequence to a provided precision
"""

def get_user_input():
    """
    Determines how many iterations to create
    """
    while True:
        try:
            input = int(raw_input("How many iterations of the Fibonacci sequence would you like?"))
        except ValueError:
            print "Please enter a number between 1 and 1,000"
            continue
        else:
            if input > 0 and input < 1000:
                break
            else:
                print "Please enter a postive number between 1 and 1,000"
                continue

    return input

def create_sequence(num):
    """
    Creates the sequence
    """
    sequence = []
    current = 1
    prev = 1
    index = 0
    sequence.append(current)
    sequence.append(prev)
    while index < num:
        temp = current + prev
        sequence.append(temp)
        prev = current
        current = temp
        index += 1
    return sequence

sequence_items = create_sequence(get_user_input())

for item in sequence_items:
    print item
