import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    chain = itertools.chain(*list_of_list)
    new_merged_list = list(chain)
    return new_merged_list
