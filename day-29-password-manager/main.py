from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    final_password = ''.join(password_list)
    pyperclip.copy(final_password)
    if password_entry.get() != 0:
        password_entry.delete(0, END)
        password_entry.insert(0, f"{final_password}")


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website_search = website_entry.get().title()
    try:
        with open("data.json", "r") as password_log:
            data = json.load(password_log)
    except FileNotFoundError:
        messagebox.showinfo(message="File not found.")
    else:
        if website_search in data:
            email = data[website_search]['email']
            password = data[website_search]['password']
            messagebox.showinfo(message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(message="Details for the website don't exist")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_input = website_entry.get().title()
    email_user_input = email_user_entry.get()
    password_input = password_entry.get()
    new_entry = {
        website_input: {
            "email": email_user_input,
            "password": password_input,
        }
    }

    if len(website_input) == 0 or len(email_user_input) == 0 or len(password_input) == 0:
        messagebox.showinfo(message="Please fill out all fields!")

    else:
        try:
            with open("data.json", "r") as entry_log:
                # Reading old data
                data = json.load(entry_log)
        except FileNotFoundError:
            with open("data.json", "w") as entry_log:
                json.dump(new_entry, entry_log, indent=4)
        else:
            # Updating old data with new data
            data.update(new_entry)
            with open("data.json", "w") as entry_log:
                # Saving updated data
                json.dump(data, entry_log, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#dddddd")

canvas = Canvas(width=200, height=200, bg="#dddddd", highlightthickness=0)
lock_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="#dddddd", highlightthickness=0)
website_label.grid(column=0, row=1)
email_user_label = Label(text="Email/Username:", bg="#dddddd", highlightthickness=0)
email_user_label.grid(column=0, row=2)
password_label = Label(text="Password: ", bg="#dddddd", highlightthickness=0)
password_label.grid(column=0, row=3)

website_entry = Entry(width=21, highlightthickness=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_user_entry = Entry(width=35, highlightthickness=0)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "ab.luis04@gmail.com")

password_entry = Entry(width=21, highlightthickness=0)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", width=14, highlightthickness=0, command=find_password)
search_button.grid(column=2, row=1)
generate_pass_button = Button(text="Generate Password", width=14, highlightthickness=0, command=generate_password)
generate_pass_button.grid(column=2, row=3)
add_pass_button = Button(text="Add", width=36, highlightthickness=0, command=save)
add_pass_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
