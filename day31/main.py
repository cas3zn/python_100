from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
random_index = {}

try:
    data = pandas.read_csv("data/known_words.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def next_card():
    """
        Once the user presses the 'right' button, a random dictionary is selected from
        the data and the French word from the dict is displayed on the canvas.
    """
    global random_index, flip_timer
    window.after_cancel(flip_timer)
    random_index = random.choice(data_dict)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_content, text=random_index["French"], fill="black")
    canvas.itemconfig(canvas_front, image=front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    """
        The English word in the random dictionary is displayed after 3 seconds
    """
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_content, text=random_index["English"], fill="white")
    canvas.itemconfig(canvas_front, image=back_image)


def is_known():
    """
        Called when the left button is clicked.
        It removes the random dictionary from the data.
        A new CSV file is created where the random dict is added
        The next_card() is called
    """
    data_dict.remove(random_index)
    next_card()
    new_csv = pandas.DataFrame(data_dict)
    new_csv.to_csv("data/known_words.csv", index=False)


# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_front = canvas.create_image(400, 263, image=front_image)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_content = canvas.create_text(400, 280, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
known_image = PhotoImage(file="images/right.png")
known_button = Button(image=known_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

unknown_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()
window.mainloop()
