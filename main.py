from tkinter import *
from tkinter import messagebox
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"


data = pd.read_csv("data/dictionary.csv")
dictionary = data.to_dict(orient="records")
current_card = {}
old_card = []


def next_card():
    global current_card, old_card

    if len(old_card) == len(dictionary):
        messagebox.showinfo(title="Game's Over", message="You won")
        window.destroy()

    current_card = random.choice(dictionary)
    while current_card in old_card:
        current_card = random.choice(dictionary)
    old_card.append(current_card)
    


    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card['English'], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)

    

def flip_card():
    global current_card

    canvas.itemconfig(card_title, text = "Vietnamese", fill="white")
    canvas.itemconfig(card_word, text=current_card['Vietnamese'], fill="white")
    canvas.itemconfig(card_bg, image=card_bg_img)

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_bg_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Aril", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Aril", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

cross_image = PhotoImage(file="images/wrong.png")
unknown_btton = Button(image=cross_image, highlightthickness=0, command=flip_card)
unknown_btton.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()


window.mainloop()