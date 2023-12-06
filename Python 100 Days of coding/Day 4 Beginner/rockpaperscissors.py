# Rock paper scissors exercise 
#   Review

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_ops = [rock, paper, scissors]

userchoice = int(input("Choose Rock (0), Paper (1), or Scissors (2): "))

if userchoice >= 3 or userchoice < 0:
    print("That is not a valid option. You lose!")
    exit(1)

print("You chose\n" + game_ops[userchoice])

computerchoice = random.randint(0,2)
print("Computer chose\n" + game_ops[computerchoice])
if userchoice == 0 and computerchoice == 2:
  print("You win!")
elif computerchoice == 0 and userchoice == 2:
  print("You lose")
elif computerchoice > userchoice:
  print("You lose")
elif userchoice > computerchoice:
  print("You win!")
elif computerchoice == userchoice:
  print("It's a draw")