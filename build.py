import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    '''
    Enter your code here
    '''
    new_merged_list = [item for sublist in list_of_list for item in sublist]
    return new_merged_list
