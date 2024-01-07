from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 14, 'italic')


class QuizUI:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        quiz_icon = PhotoImage(file='images/icons8-quiz-96.png')
        self.window.wm_iconphoto(False, quiz_icon)
        self.window.config(padx=20, pady=20, background=THEME_COLOR)
        self.score_label = Label(text='Score: 0', background=THEME_COLOR, foreground='white', font=FONT)
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=250, text='Questions will appear here!', font=FONT)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = PhotoImage(file='images/true.png')
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.correct_button)
        self.correct_button.grid(column=0, row=2)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.wrong_button)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            question = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You've reached the end of the quiz!\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.correct_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def correct_button(self):
        is_true = self.quiz.check_answer('true')
        self.give_feedback(is_true)

    def wrong_button(self):
        is_true = self.quiz.check_answer('false')
        self.give_feedback(is_true)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(background='green')
        else:
            self.canvas.config(background='red')
        self.window.after(1000, func=self.get_next_question)
