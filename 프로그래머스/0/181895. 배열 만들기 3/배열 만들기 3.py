def solution(arr, intervals):
    answer = []
    for a,b in intervals:
        # append X
        # use extend to add at once 
        answer.extend(arr[a:b+1])
    return answer