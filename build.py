import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    new_merged_list = []
    for item in list_of_list:
        new_merged_list += item
    return new_merged_list
