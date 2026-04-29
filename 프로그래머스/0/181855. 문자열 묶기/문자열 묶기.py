def solution(strArr):
    str_length = []
    for string in strArr:
        str_length.append(len(string))
    
    count_length = {}
    for i in str_length:
        if i in count_length:
            count_length[i] += 1
        else:
            count_length[i] = 1
    return max(count_length.values())