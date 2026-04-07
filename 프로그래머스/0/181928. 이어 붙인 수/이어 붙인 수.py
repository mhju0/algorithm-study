def solution(num_list):
    # join 연습 
    odd = int(''.join(str(n) for n in num_list if n % 2 == 1))
    even = int(''.join(str(n) for n in num_list if n % 2 == 0))
    return odd + even