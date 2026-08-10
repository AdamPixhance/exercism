min = 1
max = 64
def square(number):
    if (number < min) or (number > max):
        raise ValueError("square must be between 1 and 64")
    else:
        return 2**(number-1)
    


def total():
    total = 0
    for x in range(min, max+1):
        total += square(x)
    return total