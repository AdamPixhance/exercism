import string


question_response = "Sure."
yell_response = "Whoa, chill out!"
yell_question_response = "Calm down, I know what I'm doing!" 
silent_response = "Fine. Be that way!"
else_response = "Whatever."

def response(hey_bob):
    isQuestion = False
    isYell = False
    isSilent = True
    for x in hey_bob:
        if hey_bob == "":
            return silent_response
        for x in hey_bob:
            if x not in string.whitespace:
                isSilent = False
    if isSilent:
        return silent_response
    for x in hey_bob.strip():
        if x == '?':
            isQuestion = True
        else:
            isQuestion = False
    
    for x in hey_bob:
        if ord(x) > 64 and ord(x) < 90:
            isYell = True
    for x in hey_bob:
        if ord(x) > 96 and ord(x) < 123:
            isYell = False
    
    if isQuestion and isYell:
        return yell_question_response
    elif isQuestion:
        return question_response
    elif isYell:
        return yell_response
    return else_response