def equilateral(sides):
    a = float(sides [0])
    b = float(sides [1])
    c = float(sides [2])
    if (a == 0 and b == 0 and c == 0):
        return False
    return a == b and b == c

def isosceles(sides):
    if equilateral(sides):
        return True
    a = float(sides [0])
    b = float(sides [1])
    c = float(sides [2])
    isIsoleces =((a == b) or (a == c) or (b == c))
    return isIsoleces

def scalene(sides):
    if not isosceles(sides):
        return True
    else:
        return False