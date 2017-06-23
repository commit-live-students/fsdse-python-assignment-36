original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

def solution(list_of_list):
    new_merged_list = []
    # list_num = [[1,2,3],[4,5],[6],[7],[8,9]]
    for elem in list_of_list:
        for num in elem:
            new_merged_list.append(num)
    # print concat_num
    return new_merged_list

solution(original_list)
