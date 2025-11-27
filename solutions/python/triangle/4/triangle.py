def is_valid(sides):
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0
        and a+b >= c and a+c >= b and b+c >= a
    )


def equilateral(sides):
    a, b, c = sides
    return is_valid(sides) and a == b and b == c

def isosceles(sides):
    a, b, c = sides
    return equilateral(sides) or (is_valid(sides) and ((a == b) or (a == c) or (b == c)))

def scalene(sides):
    return is_valid(sides) and not isosceles