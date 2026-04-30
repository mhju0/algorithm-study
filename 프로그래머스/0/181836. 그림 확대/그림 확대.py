def solution(picture, k):
    result_arr = []
    for i in picture:
        pic_str = ''
        for j in i:
            pic_str += (j * k)
        for x in range(k):
            result_arr.append(pic_str)
    return result_arr
    
        