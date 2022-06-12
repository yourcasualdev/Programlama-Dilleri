def fixstart(s):
    letter = s[0]
    new_string = letter + s[1:].replace(letter, '*')
    return new_string


print(fixstart(input("")))
