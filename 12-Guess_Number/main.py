# Import the logo and the 'random' module
from art import logo
import os
import random

def game():
  def easy_level():
    """
      This function will give the user 10 attempts to guess the correct number.
    
    Step 1: Create local variables game_over, correct_answer(randint function) & attempts
    Step 2: Create a while loop to run until the user finishes the game.
    Step 3: Inside the loop, make the user guess. Store it in a 'guess' variable and convert it into an int
    Step 4: Using if-else statement, check if attempts are higher than one. Else, finish game. User loses
    Step 5: Using if-else statement inside step 5, check if guess is equal to correct_number. Else, continue looping until user guesses the correct number.
    Step 6: Using if-else statement inside step 6, check if guess is higher than correct number and print 'Too High. Guess again'. Else print 'Too Low. Guess again.'
    """
    print("Pick a number between 1 and 100.\nYou have 10 attempts remaining.")
    
    attempts = 10
    correct_number = random.randint(1, 100)
    game_over = False
    
    while not game_over:
      guess = int(input("Make a guess: "))
      if attempts > 1:
        if guess != correct_number:
          if guess > correct_number:
            print("Too High.\nGuess again.\n")
          else:
            print("Too Low.\nGuess again.\n")
          attempts -=1
          print(f"You got {attempts} attempt(s) remaining.")
        else:
          print(f"\nYou got it! The number was {correct_number}.")
          game_over = True
      else:
        print("Game over. You ran out of attempts")
        game_over = True
    
  def hard_level():
    """
    This function will give the user 5 attempts to guess the correct number.
    
    Step 1: Create local variables game_over, correct_answer(randint function) & attempts
    Step 2: Create a while loop to run until the user finishes the game.
    Step 3: Inside the loop, make the user guess. Store it in a 'guess' variable and convert it into an int
    Step 4: Using if-else statement, check if attempts are higher than one. Else, finish game. User loses
    Step 5: Using if-else statement inside step 5, check if guess is equal to correct_number. Else, continue looping until user guesses the correct number.
    Step 6: Using if-else statement inside step 6, check if guess is higher than correct number and print 'Too High. Guess again'. Else print 'Too Low. Guess again.'
    """
  
    print("Pick a number between 1 and 100.\nYou have 5 attempts remaining.")
    
    attempts = 5
    correct_number = random.randint(1, 100)
    game_over = False
    
    while not game_over:
      guess = int(input("Make a guess: "))
      if attempts > 1:
        if guess != correct_number:
          if guess > correct_number:
            print("Too High.\nGuess again.\n")
          else:
            print("Too Low.\nGuess again.\n")
          attempts -=1
          print(f"You got {attempts} attempt(s) remaining.")
        else:
          print(f"\nYou got it! The number was {correct_number}.")
          game_over = True
      else:
        print("Game over. You ran out of attempts")
        game_over = True
  
  os.system('cls')
  print(logo)
  print("Welcome to The Number Guessing Game!")
  difficulty = input("Please choose a difficulty level. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    easy_level()
  elif difficulty == 'hard':
    hard_level()
  else:
    print('Please pick a valid level.')
    
game()