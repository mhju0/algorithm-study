def solution(myString, pat):
    new_string = myString.replace("A", "X").replace("B","A").replace("X","B")
    return 1 if pat in new_string else 0 