from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND = "#FFFFFF"
FONT = ("Ariel", 30, "italic")
# --------------------------------------UI----------------------------------


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=600, height=700)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=1, columnspan=3, pady=20, padx=50)

button_image_1 = PhotoImage(file="./images/wrong.png")
button = Button(image=button_image_1, highlightthickness=0)
button.grid(row=1, column=1, padx=150)

button_image_2 = PhotoImage(file="./images/right.png")
button = Button(image=button_image_2, highlightthickness=0)
button.grid(row=1, column=2, padx=50)

label_language = Canvas(height=526, width=800, background=WHITE_BACKGROUND)
label_language.create_text(400, 153,text="Name", font=FONT)
label_language.create_text(400, 263,text="Name", font=FONT)
label_language.grid(row=0, column=1, columnspan=3)

# label_word = Canvas()
# label_word.create_text(400, 263, text="Hello", font=FONT)
# label_word.grid(row=0, column=1, columnspan=3)

window.mainloop()
