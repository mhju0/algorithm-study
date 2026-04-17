def solution(arr):
    counter = 0 
    while True:
        old_arr = arr[:]
        for i, v in enumerate(arr):
            if v >= 50 and v % 2 == 0:
                arr[i] //= 2
            elif v < 50 and v % 2 == 1:
                arr[i] = arr[i] * 2 + 1
        if old_arr == arr:
            return counter
        counter += 1

            
            