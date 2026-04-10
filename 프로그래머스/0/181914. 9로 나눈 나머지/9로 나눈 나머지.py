# 1번 방법
# def solution(number):
#     total = 0
#     for n in str(number):
#         total += int(n)
#     answer = total % 9
#     return answer

# map() 방법
# def solution(number):
#     return sum(map(int, number)) % 9

def solution(number):
    return sum(int(n) for n in number) % 9