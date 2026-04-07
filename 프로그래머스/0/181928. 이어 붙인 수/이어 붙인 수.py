def solution(num_list):
    odd = ''
    even = ''
    for a in num_list:
        if a % 2 == 1:
            odd += str(a)
        else:
            even += str(a)
    return int(odd) + int(even)