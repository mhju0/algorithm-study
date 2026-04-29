from collections import Counter
def solution(strArr):
    return max(Counter(len(s) for s in strArr).values())