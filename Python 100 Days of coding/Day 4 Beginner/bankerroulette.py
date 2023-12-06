# Review
# Banker Roulette
import random
names_string = input("Give a list of names separated by a comma and a space: ")

names = names_string.split(", ")
# total num of items in list
num_items = len(names)
#generate random numbers between 0 and last index
rand_choice = random.randint(0, num_items-1)
#Pick random person who will pay
personpays = names[rand_choice]

print(personpays + " is covering the bill!")