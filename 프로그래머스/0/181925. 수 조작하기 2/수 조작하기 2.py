def solution(numLog):
    answer = ''
    for n in range(len(numLog) - 1):
        difference = numLog[n+1] - numLog[n]
        if difference == 1:
            answer += 'w'
        elif difference == -1:
            answer += 's'
        elif difference == 10:
            answer += 'd'
        elif difference == -10:
            answer += 'a'
    return answer