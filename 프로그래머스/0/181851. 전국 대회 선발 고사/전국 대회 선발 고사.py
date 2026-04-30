def solution(rank, attendance):
    result = []
    for i, (r,a) in enumerate(zip(rank,attendance)):
        if a:
            result.append((r,i))
    result.sort()
    
    a, b, c = result[0][1], result[1][1], result[2][1]
    
    return 10000 * a + 100 * b + c
