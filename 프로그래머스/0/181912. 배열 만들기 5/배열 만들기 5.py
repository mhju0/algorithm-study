# def solution(intStrs, k, s, l):
#     answer = []
#     for n in intStrs:
#         if int(n[s:s+l]) > k:
#             answer.append(int(n[s:s+l]))
#     return answer

def solution(intStrs, k, s, l):
    return [int(n[s:s+l]) for n in intStrs if int(n[s:s+l]) > k]