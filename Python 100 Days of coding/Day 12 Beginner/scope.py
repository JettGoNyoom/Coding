#Modifying global scope

enemies = 1
print(f"Enemies before function: {enemies}")

# B A D  P R A C T I C E
def increase_enemies():
    #have to explicitly describe global variable to be modified
    global enemies
    enemies += 1
    print(f"Enemies inside bad function: {enemies}")

increase_enemies()
print(f"Enemies outside bad function: {enemies}")

# Good practice
def increase_enemies2():
    #have to explicitly describe global variable to be modified
    print(f"Enemies inside good function: {enemies}")
    return enemies + 1
enemies = increase_enemies2()
print(f"Enemies outside good function: {enemies}")

