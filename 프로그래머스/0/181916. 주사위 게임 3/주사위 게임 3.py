def solution(a, b, c, d):
    counts = {}
    for n in [a, b, c, d]:
        counts[n] = counts.get(n, 0) + 1

    size = len(set([a, b, c, d]))

    if size == 1:
        return 1111 * a
    if size == 4:
        return min(a, b, c, d)
    if size == 2 and 3 in counts.values():
        p = next(k for k, v in counts.items() if v == 3)
        q = next(k for k, v in counts.items() if v == 1)
        return (10 * p + q) ** 2
    if size == 2:
        p, q = [k for k, v in counts.items() if v == 2]
        return (p + q) * abs(p - q)
    if size == 3:
        q, r = [k for k, v in counts.items() if v == 1]
        return q * r