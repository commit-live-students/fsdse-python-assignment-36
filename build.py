import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    new_merged_list=[]
    for x in list_of_list:
        if isinstance(x,list):
            new_merged_list.extend(solution(x))
        else:
            new_merged_list.append(x)
    return new_merged_list
