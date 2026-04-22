import re

def solution(myStr):
    myList = [i for i in re.split('a|b|c', myStr) if i != '']
    return myList if myList else ["EMPTY"]