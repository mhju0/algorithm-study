def solution(arr, n):
    if len(arr) % 2 == 0:
        x = 1
        while x <= len(arr):
            arr[x] += n
            x += 2
    else:
        x = 0
        while x <= len(arr):
            arr[x] += n
            x += 2    
    return arr