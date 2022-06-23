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

#Write your code below this line 👇
user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
userInput_int = int(user_input)
computer_input = random.randint(0, 2)

if userInput_int == 0 and computer_input == 1:
  print(f"{rock}\nComputer chose: \n{paper}\nYou lose.")
elif userInput_int == 1 and computer_input == 0:
  print(f"{paper}\nComputer chose: \n{rock}\nYou Win!")
elif userInput_int == 2 and computer_input == 1:
  print(f"{scissors}\nComputer chose: \n{paper}\nYou Win!")
elif userInput_int == 1 and computer_input == 2:
  print(f"{paper}\nComputer chose: \n{scissors}\nYou lose.")
elif userInput_int == 2 and computer_input == 0:
  print(f"{scissors}\nComputer chose: \n{rock}\nYou lose.")
elif userInput_int == 0 and computer_input == 0:
  print(f"{rock}\nComputer chose: \n{rock}\nIt's a draw")
elif userInput_int == 1 and computer_input == 1:
  print(f"{paper}\nComputer chose: \n{paper}\nIt's a draw")
elif userInput_int == 2 and computer_input == 2:
  print(f"{scissors}\nComputer chose: \n{scissors}\nIt's a draw")
else:
  print(f"{rock}\nComputer chose: \n{scissors}\nYou Win!")