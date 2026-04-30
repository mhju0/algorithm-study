def solution(myString):
    return ''.join(map(lambda letter: letter if letter >= 'l' else 'l', myString))