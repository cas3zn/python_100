############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

import random
import os
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_card = random.choice(cards)
  return random_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
    
  if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
  sum_of_cards = sum(cards)   
  return sum_of_cards


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "It's a draw"
  elif user_score == 0:
    return "Blackjack! You win."
  elif computer_score == 0:
    return "You lose! Opponent has blackjack."
  elif user_score > 21:
    return "You went over. You lose."
  elif computer_score > 21:
    return "Opponent went over. You win."
  elif user_score > computer_score:
    return "You win."
  else:
    return "You lose."


def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  end_of_game = False
  #Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not end_of_game:
    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    user_score = calculate_score(user_cards)
    cpu_score = calculate_score(computer_cards)
    print(f"  Your cards: {user_cards}, your total: {user_score}\n  Computer's first card: {computer_cards[0]}")
    if user_score == 0 or cpu_score == 0 or user_score > 21:
      end_of_game = True
    #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    else:
      ask = input('Would you like to draw another card? yes or no: ')
      if ask == 'yes':
        user_cards.append(deal_card())
      else:
        end_of_game = True
  

  while cpu_score != 0 and cpu_score < 17:
    computer_cards.append(deal_card())
    cpu_score = calculate_score(computer_cards)
  
  print(f"  Your first hand: {user_cards}, final score: {user_score}")
  print(f"  Computer's first hand: {computer_cards}, final score: {cpu_score}")
  print(compare(user_score=user_score, computer_score=cpu_score))

  
while input("Would you like to play a game of blackjack? Type 'y' or 'n': ") == 'y':
  os.system('cls')
  play_game()
