def solution(num_list):
    counter = 0
    for i,v in enumerate(num_list):
        while v != 1:
            if v % 2 == 0:
                v //= 2
            elif v % 2 == 1:
                v = (v-1) / 2
            counter += 1
    return counter