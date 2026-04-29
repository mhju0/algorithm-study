def solution(strArr):
    count_length = {}
    for s in strArr:
        count_length[len(s)] = count_length.get(len(s), 0) + 1
    return max(count_length.values())