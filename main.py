from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# --------------------------------------UI----------------------------------


window = Tk()
window.title("Flash Card")
window.config(bg=BACKGROUND_COLOR)
window.minsize(width=800, height=600)

canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_image = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 263, image=card_image)
canvas.grid(row=0, column=0, pady=40, padx=40)

window.mainloop()
