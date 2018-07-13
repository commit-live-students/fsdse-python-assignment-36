import itertools

original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

def solution(list_of_list):
    new_merged_list=[]
    for v in list_of_list:
        for v1 in v:
            new_merged_list.append(v1)
    return new_merged_list

print solution(original_list)
