prog_dict = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(prog_dict["Function"])

#Adding to dict\

prog_dict["Loop"] = "The action of doing something over and over again."
print(prog_dict)

# Creating empty dictionary
empty_dict = {}
# Can also wipe an existing dictionary by setting existing dictionary = {}

#Loop thru dict
for key in prog_dict:
    print(key)
    print(prog_dict[key])