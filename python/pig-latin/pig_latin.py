import string
vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
qu = ['q', 'Q', 'u', 'U']


def extra_words(text):
    tempWord = ""
    words_list = []
    for x in text:
        if x not in string.whitespace:
            tempWord += x
        else:
            words_list.append(tempWord)
            tempWord = ""
    return words_list

def add_ayy(word):
    word += "ay"
    return word

def move_consonants_end(word):
    temp_consonants = ""
    temp_counter = 0
    for x in word:
        if x not in vowels:
            temp_consonants += x
            temp_counter += 1
        else:
            word = word[temp_counter:]
            word += temp_consonants
            word += "ay"
            return word

def move_qu(word):
    temp_consonants = ""
    temp_counter = 0
    for x in word:
        if x not in qu:
            temp_consonants += x
            temp_counter += 1
        else:
            word = word[temp_counter:]
            word += temp_consonants
            return word







def translate(text):
    pass
