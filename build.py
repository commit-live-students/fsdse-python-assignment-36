import itertools

ol = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]


def solution(l):
    nml = []
    for i in range(0,len(ol)):
        for j in range(0,len(ol[i])):
            nml.append(ol[i][j])
    print nml
    return nml

solution(ol)
