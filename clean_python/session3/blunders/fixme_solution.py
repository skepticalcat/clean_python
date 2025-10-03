from statistics import mean #FIXED: wildcard import removed



def generate_statistics(matrix: list[list], result=None): #FIXED: removed mutable default param
    if not result: #FIXED: do this instead
        result = []
    if matrix == [[0],[0]]: #FIXED: == instead if is to check for logical equvialency
        return "Pointless to generate statistics"
    my_list = [] #FIXED: renamed list to not shadow builtin
    #FIXED: removed pointless try/catch, but if your function could produce, e.g., a DivisionByZero, catch that
    #and handle it
    for column in matrix:
        result.append(sum(column))
        my_list.append(mean(column))
    return result, my_list


input = [[1, 2, 3], [4, 5, 6]]

print(generate_statistics(input))