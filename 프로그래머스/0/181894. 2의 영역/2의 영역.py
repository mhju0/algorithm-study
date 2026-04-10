def solution(arr):
    list_answer = [i for i, v in enumerate(arr) if v == 2]
    if list_answer == []:
        return [-1]
    elif len(list_answer) == 1:
        return [2]
    else:
        return arr[list_answer[0]:list_answer[-1]+1]