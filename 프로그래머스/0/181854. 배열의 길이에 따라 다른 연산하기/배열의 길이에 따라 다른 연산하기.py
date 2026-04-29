def solution(arr, n):
    x = 1 if len(arr) % 2 == 0 else 0
    while x < len(arr):
            arr[x] += n
            x += 2  
    return arr