import tkinter
from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)


        #score label
        self.score_label = Label(self.window, text="Score: ", fg="white", bg=THEME_COLOR, font=("Arial", 20))
        self.score_label.grid(column=1, row=0)

        #canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="some Question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #wrong button
        cross_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=cross_image)
        self.wrong_button.config(bg = THEME_COLOR, highlightthickness=0)
        self.wrong_button.grid(column=0, row=2)

        #right button
        check_mark_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=check_mark_image)
        self.right_button.config(bg = THEME_COLOR, highlightthickness=0)
        self.right_button.grid(column=1, row=2)



        self.window.mainloop()