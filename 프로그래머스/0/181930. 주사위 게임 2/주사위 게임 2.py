def solution(a, b, c):
    s3 = a + b + c
    s2 = s3 * (a**2 + b**2 + c**2)
    s1 = s2 * (a**3 + b**3 + c**3)
    unique = len(set([a, b, c]))
    if unique == 1: return s1
    if unique == 2: return s2 
    if unique == 3: return s3