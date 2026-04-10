def solution(number):
    sum_digits = 0
    for n in str(number):
        sum_digits += int(n)
    answer = sum_digits % 9
    return answer