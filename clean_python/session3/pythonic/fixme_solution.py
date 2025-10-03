def find_largest_in_csv():

    with open("inputdata.csv", "r") as rh: #FIXED: context manager usage
        content = rh.readlines()

    if any(not x.isdigit() for x in content): #FIXED: pointless, but shows useage of any()
        return max([int(y) for y in content if y.isdigit()]) #FIXED: nice loop with list comprehension
    else:
        return max(content) #FIXED: builtin used



print(find_largest_in_csv())