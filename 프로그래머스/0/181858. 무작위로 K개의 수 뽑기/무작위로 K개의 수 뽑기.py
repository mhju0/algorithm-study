def solution(arr, k):
    result = []
    seen = set()
    for v in arr:
        if len(result) == k:
            break
        if v not in seen:
            seen.add(v)
            result.append(v)
    result += [-1] * (k - len(result))
    return result
