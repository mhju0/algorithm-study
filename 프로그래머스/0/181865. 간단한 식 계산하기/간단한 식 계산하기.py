def solution(binomial):
    new_list = binomial.split(" ")
    if new_list[1] == "+":
        return int(new_list[0]) + int(new_list[2])
    elif new_list[1] == "-":
        return int(new_list[0]) - int(new_list[2])
    elif new_list[1] == "*":
        return int(new_list[0]) * int(new_list[2])