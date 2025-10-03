from statistics import *



def generate_statistics(matrix: list[list], result=[]):
    if matrix is [[0],[0]]:
        return "Pointless to generate statistics"
    list = []
    try:
        for column in matrix:
            result.append(sum(column))
            list.append(mean(column))
        return result, list
    except:
        ...


input = [[1, 2, 3], [4, 5, 6]]

print(generate_statistics(input))