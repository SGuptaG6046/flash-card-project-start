from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
try:
        data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
        data = pd.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}
def next_card():
        global current_card, flip_timer, to_learn
        gui.after_cancel(flip_timer)
        current_card = choice(to_learn)
        canvas.itemconfig(title, text = "French", fill= "black")
        canvas.itemconfig(word, text = current_card["French"], fill= "black")
        canvas.itemconfig(card_background, image=front_img)
        flip_timer = gui.after(3000, func=flip_card)


def flip_card():
        canvas.itemconfig(title, text = "English", fill = "white")
        canvas.itemconfig(word, text = current_card["English"], fill = "white")
        canvas.itemconfig(card_background, image = back_img)

def to_known():
        to_learn.remove(current_card)
        print(len(to_learn))
        learn_data = pd.DataFrame(to_learn)
        learn_data.to_csv("./data/words_to_learn.csv", index=False)
        next_card()

gui = Tk()
gui.title("Flashy")
gui.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = gui.after(3000, func=next_card)

# Create Canvas
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image = front_img)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img,highlightthickness=0, command=to_known)
right_button.grid(row=1, column=1)
next_card()
gui.mainloop()