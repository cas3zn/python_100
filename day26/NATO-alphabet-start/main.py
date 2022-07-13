# Create a dictionary in this format:
import pandas
csv = pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(csv)

new_dictionary = {row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type in a random word.").upper()
new_list = [new_dictionary[letter] for letter in user_input]

print(new_list)
