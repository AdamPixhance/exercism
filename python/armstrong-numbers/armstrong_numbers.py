def is_armstrong_number(number):
    sum = 0
    numberString = str(number)
    length = len(numberString)
    for x in numberString:
        intValue = ord(x) - ord('0')
        sum += intValue**length
    return sum == number