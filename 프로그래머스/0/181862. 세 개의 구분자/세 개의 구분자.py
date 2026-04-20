import re

def solution(myStr):
    myList = [i for i in re.split(r'[abc]', myStr) if i != '']
    return myList if myList else ["EMPTY"]