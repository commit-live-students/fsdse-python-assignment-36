import operator
def solution(list_of_list):
    '''
    Enter your code here
    '''
    new_merged_list = reduce(operator.concat, list_of_list)
    return new_merged_list
