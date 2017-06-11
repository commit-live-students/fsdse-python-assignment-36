import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    '''
    Enter your code here
    '''
    new_merged_list = []
    for list1 in list_of_list:
        for i in list1:
            new_merged_list.append(i)
    return new_merged_list

#print(solution(original_list))
