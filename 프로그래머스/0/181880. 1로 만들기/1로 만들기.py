def solution(num_list):
    counter = 0
    for v in num_list:
        while v != 1:
            v = v // 2 if v % 2 == 0 else (v-1) // 2
            counter += 1
    return counter