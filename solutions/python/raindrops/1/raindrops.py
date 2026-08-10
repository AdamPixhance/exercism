def convert(number):
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
    output = ""
    if number % 3 == 0:
        output += "Pling"
    if number % 5 == 0:
        output += "Plang"
    if number % 7 == 0:
        output += "Plong"
    return output
    