def solution(arr, idx):
    return next((i for i, v in enumerate(arr) if v == 1 and i >= idx), -1)

