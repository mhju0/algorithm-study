def solution(myString):
    answer = []
    for v in myString.split("x"):
        answer.append(len(v))
    return answer