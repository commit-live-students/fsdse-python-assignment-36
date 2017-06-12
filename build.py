
from  itertools import*

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):

    new_merged_list = []
    for k in chain(list_of_list):
        for i in k:
            new_merged_list.append(i)

    #print new_merged_list
    return new_merged_list

print solution(original_list)
