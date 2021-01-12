from tkinter import *
from tkinter import messagebox
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_word = {}
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    messagebox.showinfo(message="You have reviewed all the flash cards.")
else:
    words_to_learn = data.to_dict(orient="records")


# ---------------------------- CREATE FLASH CARDS ------------------------------- #
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(words_to_learn)
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=f"{current_word['French']}", fill="black")
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FLIP CARDS ------------------------------- #
def flip_card():
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=f"{current_word['English']}", fill="white")
    window.after_cancel(next_card)


# ---------------------------- SAVE PROGRESS ------------------------------- #
def save_known_word():
    words_to_learn.remove(current_word)
    update_words_to_learn = pandas.DataFrame(words_to_learn)
    update_words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flash some Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(450, 300, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)

language_text = canvas.create_text(450, 160, text="", font=LANGUAGE_FONT)
word_text = canvas.create_text(450, 300, text="", font=WORD_FONT)

wrong_image = PhotoImage(file="images/wrong.png")
red_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
red_button.grid(column=0, row=1)
right_image = PhotoImage(file="images/right.png")
green_button = Button(image=right_image, highlightthickness=0, command=save_known_word)
green_button.grid(column=1, row=1)

next_card()

window.mainloop()
