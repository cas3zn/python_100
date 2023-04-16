""" LAYOUT AND DESIGN """

from tkinter import *

# Initialize window with title & window size
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# label
my_label = Label(text="A label", font=("Times New Roman", 24, "normal"))
my_label.config(text="config text", padx=50)
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

# Button
button = Button(text="button")
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="new button")
new_button.grid(column=2, row=0)

# Entry
input_entry = Entry(width=10)
print(input_entry.get())
# input.pack()
input_entry.grid(column=3, row=2)

window.mainloop()
