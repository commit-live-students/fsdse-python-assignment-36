import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    '''
    Enter your code here
    '''
    new_merged_list = []
    for i in original_list:
        for j in i:
            new_merged_list.append(j)
    return new_merged_list
