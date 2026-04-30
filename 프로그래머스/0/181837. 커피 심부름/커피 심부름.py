def solution(order):
    total = 0
    for i in order:
        if "cafelatte" in i:
            total += 5000
        else:
            total += 4500
    return total