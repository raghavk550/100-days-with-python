import tkinter
from tkinter import PhotoImage
import pandas, random
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"
FRENCH = "French"
ENGLISH = "English"

try:
    data_frame = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError, EmptyDataError:
    data_frame = pandas.read_csv("./data/french_words.csv")
    data_frame.to_csv("./data/words_to_learn.csv", index=False)

words_arr = data_frame.to_dict(orient="records")

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, highlightthickness=0)

random_number = random.randint(0, len(words_arr) - 1)

canvas = tkinter.Canvas(width=800, height=526)
img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=img)
title_text = canvas.create_text(400, 150, text=FRENCH, font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400, 270, text=words_arr[random_number][FRENCH], font=("Arial", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

def swap_card():
    canvas.itemconfig(canvas_img, image=back_img)
    canvas.itemconfig(title_text, text=ENGLISH, fill="white")
    canvas.itemconfig(word_text, text=words_arr[random_number][ENGLISH], fill="white")

def reset_card():
    canvas.itemconfig(canvas_img, image=img)
    canvas.itemconfig(title_text, text=FRENCH, fill="black")

def wrong_pressed():
    reset_card()
    global random_number, flip_timer
    window.after_cancel(flip_timer)
    random_number = random.randint(0, len(words_arr) - 1)
    word = words_arr[random_number]
    canvas.itemconfig(word_text, text=word[FRENCH], fill="black")
    flip_timer = window.after(3000, func=swap_card)

def right_pressed():
    reset_card()
    global random_number, flip_timer
    window.after_cancel(flip_timer)
    words_arr.pop(random_number)
    random_number = random.randint(0, len(words_arr) - 1)
    word = words_arr[random_number]
    canvas.itemconfig(word_text, text=word[FRENCH], fill="black")
    pandas.DataFrame(words_arr).to_csv("./data/words_to_learn.csv", index=False)
    flip_timer = window.after(3000, func=swap_card)

cross_img = PhotoImage(file="./images/wrong.png")
cross_button = tkinter.Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong_pressed)
cross_button.grid(row=1, column=0, pady=20)

right_img = PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right_pressed)
right_button.grid(row=1, column=1, pady=20)

flip_timer = window.after(3000, func=swap_card)

window.mainloop()