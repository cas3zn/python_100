# * Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("input/letters/starting_letter.txt") as starting_letter:
    starting_letter_contents = starting_letter.read()
    invited_names = open("input/names/invited_names.txt")
    invite = invited_names.readlines()
    print(invite)
    for line in invite:
        line_strip = line.strip()
        replaced_name = starting_letter_contents.replace("[name]", line_strip)
        with open(f"./Output/ReadyToSend/letter_to_{line_strip}.txt", "w") as new_letters:
            new_letters.write(replaced_name)

    invited_names.close()
