############DEBUGGING#####################

# # ORIGINAL CODE
# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()
# Problem is that range(x,y) does not include y
# Fixed code: if you want y included in range, it needs to be range(x,y+1)
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# # ORGINAL CODE
# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])
# Problem is that lists start at 0 index, and max index is num_items - 1. Index goes 0-5, not 1-6
# Fixed Code: change randint(1,6) to randint(0,5)
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# # ORIGINAL CODE
# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
# Problem: inputting 1994 results in NO output bc neither "year < 1994" nor "year > 1994" actually include the year 1994
# Fixed code: change "year > 1994" to "year >= 1994"
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")
# Editors will usually underline the errors it sees. if the above code were uncommented, the print statement would be underlined with red jagged lines
  # Additionally, the string in print is written like an fstring but without the f at the beginning, resulting in a bug
  # IN VSCODE: the brackets changes colors based on whether the f is present or not
    # NO F PRESENT: brackets and word inside bracket are DARK BLUE
    # F IS PRESENT: brackets are PINK, variable inside is LIGHT BLUE
  # lastly, int() needs to be added around the input statement to actually make it an INT
# Fix by adding indent to print statement
age = int(input("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# # ORIGINAL CODE
# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)
# I commonly use print statements after major operations in code to see where code stops running or which statements are not being printed bc the lines are not being run
# Print statements also useful when debugging to make sure that variables are the correct values that they should be at eact step through the code, and can identify where their intended values do not match with actual

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])
# I use debuggers only if it is dire
# Problem above: the append command into b_list is not indented properly
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

# OTHER TIPS FOR DEBUGGING:
 # 1: Take a Break
 # 2: Ask a friend (if possible)
 # 3: Run code often. I prefer to run code periodically after every couple of written lines to ensure that the lines do as i intended. the chunk size of how much to write between test runs varies per person
 # 4: STACKOVERFLOW IS ONE OF YOUR BEST FRIENDS
 # 5: Rubber Ducky Debugging 