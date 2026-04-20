def solution(strArr):
    answer = []
    for i,v in enumerate(strArr):
        if "ad" not in v:
            answer.append(v)
    return answer