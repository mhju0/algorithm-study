def solution(arr):
    i = 0
    while True:
        two = 2 ** i
        if len(arr) <= two:
            arr += [0] * (two - len(arr))
            return arr
        else:
            i += 1
    