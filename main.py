from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND = "#FFFFFF"
LANG_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 50, "bold")

# --------------------------------ACCESSING DATASET------------------------

# data = pandas.read_csv("./data/french_words.csv")
#
#
# def random_word():
#     canvas.itemconfig(card_title, text="French")
#     canvas.itemconfig(card_word, text=random.choice(data.French))

card_text = {}
to_learn = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")


def random_word():
    global card_text, timer
    window.after_cancel(timer)
    card_text = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=card_text["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=card_text["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


# ----------------------CREATING NEW DATASETS BASED ON FEEDBACK-------------
def known_words():
    to_learn.remove(card_text)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv")
    random_word()


# --------------------------------------UI----------------------------------

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)

card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)

card_title = canvas.create_text(400, 150, text="Title", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text="Name", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

button_image_1 = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=button_image_1, highlightthickness=0, command=random_word)
wrong_button.grid(row=1, column=0)

button_image_2 = PhotoImage(file="./images/right.png")
right_button = Button(image=button_image_2, highlightthickness=0, command=known_words)
right_button.grid(row=1, column=1, padx=50)

random_word()
window.mainloop()
