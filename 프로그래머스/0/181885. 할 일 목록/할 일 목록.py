# def solution(todo_list, finished):
#     unfinished = []
#     for n, m in zip(todo_list, finished):
#         if m == False:
#             unfinished.append(n)
#     return unfinished

def solution(todo_list, finished):
    return [n for n,m in zip(todo_list, finished) if not m]