# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# # Why close file?
# # To stop it from taking up resources
# file.close()

# Reading file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Will close file automatically
# 'w' will delete all in file. Will create file if it doesn't already exist
# 'a' will append
with open("my_file.txt", mode='a') as file:
    file.write("\nNew Text.")