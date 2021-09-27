# KeyError
# a_dict = {"key":"value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Orange"]
# fruit = fruit_list[2]

# TypeError
# text = "abc"
# print(text + 5)

# FileNotFound
# with open("a_file.txt") as file:
#       file.read()

# try:
#     file = open("a_file.txt")
#     a_dict = {"key":"value"}
#     print(a_dict["key"])
#
# except FileNotFoundError: # Ignore all errors when we just use expect:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message: # You can also hold the error message to use as keyword
#     print(f"The key {error_message} does not exist.")
#
# else: # If all the lines in the try block succeeded, this block works
#     content = file.read()
#     print(content)
#
# finally: # Some code that's going to run no matter what happens
#     raise KeyError("Error")

# How generate your own exceptions for unexpected situations

height = int(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters") #wrong argument


bmi = weight / height **2
print(bmi)














