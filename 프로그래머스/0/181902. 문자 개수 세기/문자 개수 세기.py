# def solution(my_string):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#     answer = [0] * 52
    
#     for n in my_string:
#         a = alphabet.index(n)
#         answer[a] += 1
    
#     return answer

def solution(my_string):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    return [my_string.count(c) for c in alphabet]