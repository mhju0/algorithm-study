def solution(arr):
    two = 1
    length_arr = len(arr)
    while two < length_arr:
        two *= 2
    return arr + [0] * (two - length_arr)
    