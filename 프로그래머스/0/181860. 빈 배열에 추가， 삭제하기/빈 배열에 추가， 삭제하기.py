def solution(arr, flag):
    answer = []
    for v,f in zip(arr,flag):
        if f:
            answer.extend([v] * (v * 2))
        else:
            del answer[-v:]
    return answer
            