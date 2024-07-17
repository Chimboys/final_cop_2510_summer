# Question:
# Use a lambda function to square each number in a list. Provide a single line of code that takes a list of numbers and returns a new list with each number squared.
# For example, if the input list is [1, 2, 3, 4], the output should be [1, 4, 9, 16].

#Example of map
# map(function_that_called_for_each_element , list_containing_elements)
#

original_list = [1,2,3,4,5]
def plus_one(x):
    return x + 1

list_plus_one = list(map(plus_one, original_list ))
print(list_plus_one)

#Instead of defining function use lambda expression to square numbers

#square_list


#Is it valid?

addition = lambda x,y,z : x+y+z
print(addition(6,7,8))























#Q1
#list_square = list(map(lambda x: x**2,original_list ))
#print(list_square)


