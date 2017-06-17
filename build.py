def solution(list_of_list):
    new_merged_list=[]
    for i in range(len(list_of_list)):
        new_merged_list.extend(list_of_list[i])
    return new_merged_list
