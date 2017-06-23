
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(list_of_list):
    final_list = []
    for sublist in list_of_list:
        for i in sublist:
            final_list.append(i)
    return final_list
