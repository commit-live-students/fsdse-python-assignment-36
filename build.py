import itertools
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]
def solution(original_list):
    new_merged_list = list(itertools.chain(*original_list))
    return new_merged_list
solution(original_list)
