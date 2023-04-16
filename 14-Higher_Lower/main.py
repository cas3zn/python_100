# To-Do List
# choose two random dictionaries from the list 'data' and compare them.
# create a loop that asks user questions as long as the user gets all the previous correct.
# Add their score by 1 to the previous score
# Display the score
# If answered wrongly, loop stops and a string with current score is printed
# If answered correctly, loop continues and current score is printed followed by another question


  # import modules
import random
from art import logo, vs
from game_data import data
  
#This function runs the game
def game():
  
  #This function compares the follower count for the two picks and returns 'A' or 'B'
  def compare():
    a = 'A'
    b = 'B'
    if pick_a['follower_count'] > pick_b['follower_count']:
      return a
    elif pick_b['follower_count'] > pick_a['follower_count']:
      return b
    else:
      a = b
      return a
  
  #This function picks a random dictionary from the list data
  def pick_choice():
    pick = random.choice(data)
    return pick
  
  #This function prints out the two comparisons in the console   
  def print_comparison(pick_1, pick_2):
    print(f"Compare A: {pick_1['name']}, a {pick_1['description']}, from {pick_1['country']}")
    print(vs)
    print(f"Against B: {pick_2['name']}, a {pick_2['description']}, from {pick_2['country']}")
  
  
  #initialize a current score and set game_over to False
  game_over = False
  current_score = 0

  #runs the game as long as user doesn't fail a comparison
  while not game_over:
      
    print(logo)
    pick_a = pick_choice()
    pick_b = pick_choice()
    print_comparison(pick_a, pick_b)
    
    user_choice = input("Who has more followers? Type 'A' or 'B'")
    correct_choice = compare()
    
    if correct_choice == user_choice:
      current_score += 1
      if current_score < 3:
        print(f'That\'s right! Current score: {current_score}')
      elif current_score < 7:
        print(f'You\'re going strong. Current score: {current_score}')
      elif current_score < 10:
        print(f'What a streak! Current score: {current_score}')
      else:
        print(f'UNSTOPPABLE! Current score: {current_score}')
    else:
      print(f'Sorry, that\'s wrong. Final score: {current_score}')
      game_over = True

game()
