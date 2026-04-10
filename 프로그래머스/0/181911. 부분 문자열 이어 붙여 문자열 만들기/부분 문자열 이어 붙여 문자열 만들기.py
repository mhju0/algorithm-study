# def solution(my_strings, parts):
#     answer = ''
#     for n, (s,e) in zip(my_strings, parts):
#         answer += n[s:e+1]
#     return answer

# one-liner version
def solution(my_strings, parts):
    return ''.join(n[s:e+1] for n, (s,e) in zip(my_strings,parts))