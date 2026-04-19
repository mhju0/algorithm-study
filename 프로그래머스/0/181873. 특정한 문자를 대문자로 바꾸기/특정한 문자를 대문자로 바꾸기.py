def solution(my_string, alp):
    string_list = list(my_string)
    for i,v in enumerate(string_list):
        if v == alp:
            string_list[i] = alp.upper()
    return "".join(string_list)