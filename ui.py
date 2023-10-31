from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.quiz.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=1, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question",
            font=("Ariel", 20, "italic"),
            fill="black",
        )

        true_button_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_button_image, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_button_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_button_image, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz.\nYour score: {self.quiz.score}",
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        answer = "True"
        self.give_feedback(answer)

    def answer_false(self):
        answer = "False"
        self.give_feedback(answer)

    def give_feedback(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
