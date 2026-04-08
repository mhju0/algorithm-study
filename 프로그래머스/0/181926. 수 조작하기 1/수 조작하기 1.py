def solution(n, control):
    delta = {'w':1, 's':-1, 'd':10, 'a':-10}
    
    for i in control:
        n += delta[i]
        
    return n