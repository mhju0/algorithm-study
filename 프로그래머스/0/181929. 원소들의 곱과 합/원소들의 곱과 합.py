def solution(num_list):
    product = 1
    sum_square = sum(num_list) ** 2
    for a in num_list:
        product *= a
    return 1 if product < sum_square else 0