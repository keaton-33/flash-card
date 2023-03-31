import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE_COLOR = "#FFFFFF"
timer = None
current_word = None
to_learn_spanish = {}

try:
    data = pandas.read_csv("./data/to_learn_spanish.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/spanish_words.csv")
    to_learn_spanish = original_data.to_dict(orient="records")
else:
    to_learn_spanish = data.to_dict(orient="records")

# spanish_words = pandas.read_csv("./data/spanish_words.csv").to_dict(orient="records")
current_language = list(to_learn_spanish[0])[0]
print(current_language)


def new_word():
    global timer, current_word
    canvas.itemconfig(canvas_image, image=card_front)
    current_index = random.randint(2, len(to_learn_spanish) - 1)
    current_word = to_learn_spanish[current_index]
    # current_word = random.choice(to_learn_spanish)
    canvas.itemconfig(word_text, text=current_word['Spanish'], fill="black")
    canvas.itemconfig(title_text, text="Spanish", fill="black")

    timer = window.after(3000, flip_card)


def flip_card():
    global current_word
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_text, text="Spanish")
    canvas.itemconfig(word_text, text=current_word['English'], fill="white")
    canvas.itemconfig(title_text, text="English", fill="white")


def check_button_pushed():
    global timer, to_learn_spanish
    window.after_cancel(timer)
    to_learn_spanish.remove(current_word)
    data = pandas.DataFrame(to_learn_spanish)
    data.to_csv("./data/to_learn_spanish.csv", index=False)
    flip_card()
    new_word()
    print(len(to_learn_spanish))


def x_button_pushed():
    global timer
    window.after_cancel(timer)
    flip_card()
    new_word()


window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title_text = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

check_image = tkinter.PhotoImage(file="./images/right.png")
check_button = tkinter.Button(image=check_image, highlightthickness=0, bd=0, command=check_button_pushed)
check_button.grid(column=1, row=1)

x_image = tkinter.PhotoImage(file="./images/wrong.png")
x_button = tkinter.Button(image=x_image, highlightthickness=0, bd=0, command=x_button_pushed)
x_button.grid(column=0, row=1)

new_word()

print(to_learn_spanish)























window.mainloop()
