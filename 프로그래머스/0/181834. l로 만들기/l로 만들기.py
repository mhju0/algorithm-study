def solution(myString):
    for letter in myString:
        if letter < 'l':
            myString = myString.replace(letter, 'l')
    return myString