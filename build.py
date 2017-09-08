import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):

    new_merged_list = []
    for i in range (0, len(list_of_list)):
        for j in range (0, len(list_of_list[i])):
            new_merged_list.append(list_of_list[i][j])

    return new_merged_list
