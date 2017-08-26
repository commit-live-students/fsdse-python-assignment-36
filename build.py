import itertools

original_list = []
new_merged_list = []

def solution(list_of_list):
    for i in list_of_list:
        for j in range(0,len(i)):
            new_merged_list.append(i[j])
    return new_merged_list

solution(original_list)
