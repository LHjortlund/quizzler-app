from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
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
            width=280,
            text="some Question text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        #wrong button
        cross_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=cross_image)
        self.wrong_button.config(bg = THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=0, row=2)

        #right button
        check_mark_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=check_mark_image)
        self.right_button.config(bg = THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of this quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
