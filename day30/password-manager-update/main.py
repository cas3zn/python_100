from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_numbers + password_letters + password_symbols
    shuffle(password_list)

    passcode = "".join(password_list)
    password_entry.insert(0, passcode)
    pyperclip.copy(passcode)


# ---------------------------- FIND PASSWORD ------------------------------ #


def find_password():
    web = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if web in data:
            messagebox.showinfo(title="Search Results", message=f"Email: {data[web]['email']}\nPassword:"
                                                                f" {data[web]['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details for {web} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    web = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "email": username,
            "password": password
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure any of the fields are not empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # read into old data
                data = json.load(data_file)
        except FileNotFoundError:
            data_file = open("data.json", "w")
            json.dump(new_data, data_file, indent=4)
            data_file.close()
        else:
            # update the old data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # write the data into the file
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)

# Labels
website_label = Label(text="Website:")
username_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

# Entries
website_entry = Entry(width=27)
website_entry.focus()
username_entry = Entry(width=50)
username_entry.insert(0, "allan01234@gmail.com")
password_entry = Entry(width=27)

# Buttons
generate_pass_btn = Button(text="Generate Password", highlightthickness=0, width=18, command=password_generator)
add_btn = Button(text="Add", width=42, command=save)
search_btn = Button(text="Search", highlightthickness=0, width=18, command=find_password)

# Grid
canvas.grid(column=1, row=0)
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

generate_pass_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn.grid(column=2, row=1)

website_entry.grid(column=1, row=1)
username_entry.grid(column=1, row=2, columnspan=2)
password_entry.grid(column=1, row=3)

window.mainloop()
