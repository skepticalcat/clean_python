

##### EXAMPLE 1 #####
# reverse this list:
to_reverse = ["Clean code makes one feel", "all warm and cozy"]
reversed = to_reverse[::-1] # or
to_reverse.reverse() # inplace!

print(reversed)

##### EXAMPLE 2 #####
# pass in the my_parameter variable using expansion
def function_taking_two_params(a, b):
    return a+b

my_parameter = ("9000", "1")
x = function_taking_two_params(*my_parameter) # your code goes here
print(x)

##### EXAMPLE 3 #####
# use a default dictionary to instantiate a dict with an empty list as default value
from collections import defaultdict
my_default_dict = defaultdict(list)

my_default_dict["hello"].append("world")
print(my_default_dict)


##### EXAMPLE 4 #####
# write a function that duplicates every value in a list and call main_function with it

def main_func(your_function):
    return your_function(["Hello", "World"])

def your_function(to_duplicate):
    return to_duplicate*2

print(main_func(your_function)) # your code also goes here, call main_func


##### EXAMPLE 5 #####
# implement the needed dunder methods (which ones?) to make our Node class comparable/sortable for weight

class MyNode:

    def __init__(self, weight: int, next=None):
        self.weight = weight
        self.next_node = next

    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        return self.weight == other.weight



node_3 = MyNode(10)
node_2 = MyNode(12, node_3)
node_1 = MyNode(-334, node_2)

list_of_nodes = sorted([node_1, node_2, node_3])
print([x.weight for x in list_of_nodes])

##### EXAMPLE 6 #####
# use zip to create a new list of tuples from the two provided lists

list_1 = [1, 2, 3]
list_2 = ["oans", "zwoa", "drei"]

list_of_tuples = list(zip(list_1, list_2))
print(list_of_tuples)
