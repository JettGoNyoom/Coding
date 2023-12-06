# Fizzbuzz game 
# Lol I hated playing this game on road trips
# Look at me now tho, I'm an engineer and a coder whose whole life revolves around math and numbers
# Aint that funny??

target = 100
for i in range(1, target+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)