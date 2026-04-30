def solution(a, b):
    odd_count = (a % 2) + (b % 2)
    if odd_count == 2:
        return a ** 2 + b ** 2
    elif odd_count == 1:
        return 2 * (a + b)
    else:
        return abs(a - b)