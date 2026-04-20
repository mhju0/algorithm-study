def solution(myString, pat):
    i = 0 
    counter = 0
    while i < len(myString):
        found = myString.find(pat, i)
        if found != -1:
            counter += 1
        else:
            return counter
        i = found + 1
    return counter