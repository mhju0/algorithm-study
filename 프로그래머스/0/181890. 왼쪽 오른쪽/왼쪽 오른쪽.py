def solution(str_list):
    loc_l = str_list.index('l') if 'l' in str_list else float('inf')  
    loc_r = str_list.index('r') if 'r' in str_list else float('inf')

    if loc_l == float('inf') and loc_r == float('inf'):
        return []
    elif loc_l <= loc_r:
        return str_list[:loc_l]
    else:
        return str_list[loc_r+1:]