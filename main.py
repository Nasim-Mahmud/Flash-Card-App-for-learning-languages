from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND = "#FFFFFF"
LANG_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 50, "bold")


# --------------------------------------UI----------------------------------

window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=600, height=700)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.create_text(300, 70,text="Title", font=LANG_FONT, )
canvas.create_text(300, 200,text="Name", font=WORD_FONT)
canvas.grid(row=0, column=0)

button_image_1 = PhotoImage(file="./images/wrong.png")
button = Button(image=button_image_1, highlightthickness=0)
button.grid(row=1, column=1, padx=150)

button_image_2 = PhotoImage(file="./images/right.png")
button = Button(image=button_image_2, highlightthickness=0)
button.grid(row=1, column=2, padx=50)


window.mainloop()
