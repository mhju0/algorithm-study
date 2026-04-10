# def solution(my_string, indices):
#     answer = ''
#     for n, m in enumerate(my_string):
#         if n not in indices:
#             answer += m
#     return answer

# set 사용해서 성능 높이기
def solution(my_string, indices):
    remove = set(indices)
    return ''.join(c for i, c in enumerate(my_string) if i not in remove)