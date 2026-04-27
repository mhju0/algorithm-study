def solution(arr, flag):
    answer = []
    for v,f in zip(arr,flag):
        if f:
            for i in range(v * 2):
                answer.append(v)
        else:
            for i in range(v):
                answer.pop()
    return answer
            