import itertools

original_list = [[2, 4, 3 , 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    new_merged_list = itertools.chain(*list_of_list)
    return list(new_merged_list)


print solution(original_list)
