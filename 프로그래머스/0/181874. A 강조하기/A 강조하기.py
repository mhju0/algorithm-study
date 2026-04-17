def solution(myString):
    result = list(myString)
    for i, v in enumerate(myString):
        if v == 'a' or v == 'A':
            result[i] = v.upper()
        else:
            result[i] = v.lower()
    return "".join(result)