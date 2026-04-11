# def solution(arr, query):
#     # enumerate 연습
#     for i,v in enumerate(query):
#         if i % 2 == 0:
#             arr = arr[:v+1]
#         else:
#             arr = arr[v:]
#     return arr
            

from functools import reduce
def solution(arr, query):
    return reduce(lambda a, t: a[:t[1]+1] if t[0]%2==0 else a[t[1]:], enumerate(query), arr)