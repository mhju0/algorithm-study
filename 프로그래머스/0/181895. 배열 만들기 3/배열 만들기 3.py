def solution(arr, intervals):
    answer = []
    for a,b in intervals:
        for i in arr[a:b+1]:
            answer.append(i)
    return answer