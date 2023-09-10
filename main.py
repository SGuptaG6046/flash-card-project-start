from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"

gui = Tk()
gui.title("Flashy")
gui.config(bg=BACKGROUND_COLOR,padx=50,pady=50)


# Create Canvas
canvas = Canvas(width=800, height=526)
back_image = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image = back_image)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 40, "italic"))
canvas.config(highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img)
right_button.grid(row=1, column=1)

gui.mainloop()