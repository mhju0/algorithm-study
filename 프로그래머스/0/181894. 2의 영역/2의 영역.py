def solution(arr):
    list_answer = [i for i, v in enumerate(arr) if v == 2]
    if not list_answer:
        return [-1]
    else:
        return arr[list_answer[0]:list_answer[-1]+1]