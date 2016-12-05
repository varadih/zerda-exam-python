# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the original list.
# It should raise an error if the parameter is not a list.
# Example: with the input [1, 2, 3, 4, 5] it should return [2, 4].

testlist = [1, 2, 3, 4, 5, 6, 7, 8]

def every_second(input_list):
    if type(input_list) is list:
        newlist = []
        for i in range(len(input_list)):
            if i % 2 == 1:
                newlist.append(input_list[i])
        return newlist
    else:
        return ('Please provide a list!')

print(every_second(testlist))
