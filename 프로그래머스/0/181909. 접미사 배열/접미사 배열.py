# def solution(my_string):
#     answer = []
#     i = 0
#     while i < len(my_string):
#         answer.append(my_string[i:])
#         i += 1
#     return sorted(answer)

def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))