def solution(arr, k):
    result = []
    for v in arr:
        if len(result) == k:
            break
        else:
            if v not in result:
                result.append(v)
    if len(result) != k:
        result += [-1] * (k - len(result))
    return result