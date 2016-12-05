# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def write_file(file_name, word):
    try:
        fw = open(file_name, "w")
        text = fw.write(word * 10)
        fw.close()
        return True
    except:
        return False

print(write_file("santa.txt", "hoohoohoo - "))
