def solution(code):
    mode = 0
    ret = ''
    for i, c in enumerate(code):
        if c == '1':
            mode = 1 - mode
        else:
            if mode == 0 and i % 2 == 0:
                ret += c
            elif mode == 1 and i % 2 == 1:
                ret += c
    return ret if ret else 'EMPTY' 