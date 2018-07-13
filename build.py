import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    l = []

    for x in list_of_list:
        for y in x:
            l.append(y)

    return l

solution(original_list)
