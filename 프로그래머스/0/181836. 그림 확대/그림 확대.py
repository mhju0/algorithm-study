def solution(picture, k):
    result_arr = []
    for row in picture:
        expanded = ''.join(j * k for j in row)
        result_arr.extend([expanded] * k)
    return result_arr
    
        