def solution(myString, pat):
    my_dict = {"A" : "B",
              "B" : "A"}
    table = myString.maketrans(my_dict)
    new_string = myString.translate(table)
    return 1 if pat in new_string else 0