import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# set end of game to false and lives to 6. This will determine end of while loop
end_of_game = False
lives = 6

print(logo)
print("Welcome to hangman!")

display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
      print(f"You have already guessed {guess}, try guessing another letter.")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      lives -= 1
      print(f"{guess} is not in the word. You have {lives} lives left.")
      if lives == 0:
          end_of_game = True
          print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
