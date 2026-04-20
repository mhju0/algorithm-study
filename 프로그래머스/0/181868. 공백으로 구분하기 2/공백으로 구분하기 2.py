def solution(my_string):
    answer = []
    for v in my_string.split(' '):
        if v != '':
            answer.append(v)
    return answer