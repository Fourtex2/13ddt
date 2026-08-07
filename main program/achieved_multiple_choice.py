import tkinter as tk
from PIL import Image, ImageTk
import random
import questions

def generate_question():
    achieved_multiple_choice = [
        questions.complex_modulus_achieved,
        questions.complex_argument_achieved,
        questions.differentiation_basic_achieved,
    ]

    question, answer = random.choice(achieved_multiple_choice)()

    return question, answer

class AchievedQuestions:
    def question_generator(self):

        question, answer = random.choice(
            self.achieved_multiple_choice
        )()

        false_answers = []

        while len(false_answers) < 3:
            _, wrong = random.choice(
                self.achieved_multiple_choice
            )()

            if wrong != answer and wrong not in false_answers:
                false_answers.append(wrong)

        self.answer_list = [answer] + false_answers
        random.shuffle(self.answer_list)

        self.question_label.config(
            text=questions.format_fixer(question)
        )

        for i, label in enumerate(self.answer_labels):
            label.config(
                text=questions.format_fixer(
                    self.answer_list[i]
                )
            )

        self.correct_answer = self.answer_list.index(answer)
        
        for label in self.answer_labels:
            label.config(bg="red")
        self.answer_labels[self.correct_answer].config(bg="green")
    

    def answer_checker(self, clicked_label):

        if clicked_label == self.answer_labels[self.correct_answer]:

            self.canvas.itemconfigure(
                self.correct_answer_window,
                state="normal"
            )

        else:

            self.canvas.itemconfigure(
                self.incorrect_answer_window,
                state="normal"
            )



    def __init__(self, canvas, root):

        self.canvas = canvas
        self.root = root

        self.timeout_status = True


        self.achieved_multiple_choice = [
            questions.complex_modulus_achieved,
            questions.complex_argument_achieved,
            questions.complex_division_achieved,
            questions.complex_quadratic_achieved,
            questions.differentiation_basic_achieved,
            questions.differentiation_chain_achieved,
            questions.complex_multiplication_achieved,
            questions.differentiation_product_achieved,
            questions.differentiation_quotient_achieved
        ]


        self.multiple_choice_questions_frame = tk.Frame(self.canvas, bg="grey")        


        self.question_label = tk.Label(self.multiple_choice_questions_frame,bg="blue")
        self.question_label.place(relx=.5,
                             rely=.2,
                             relheight=.1,
                             relwidth=.7,
                             anchor='center')

        self.answer_1_label = tk.Label(self.multiple_choice_questions_frame,bg="green")
        self.answer_1_label.place(relx=.3,
                             rely=.4,
                             relheight=.1,
                             relwidth=.3,
                             anchor='center')
        
        self.answer_2_label = tk.Label(self.multiple_choice_questions_frame,bg="green")
        self.answer_2_label.place(relx=.6,
                             rely=.4,
                             relheight=.1,
                             relwidth=.3,
                             anchor='center')
        self.answer_3_label = tk.Label(self.multiple_choice_questions_frame,bg="green")
        self.answer_3_label.place(relx=.3,
                             rely=.8,
                             relheight=.1,
                             relwidth=.3,
                             anchor='center')
        self.answer_4_label = tk.Label(self.multiple_choice_questions_frame,bg="green")
        self.answer_4_label.place(relx=.6,
                             rely=.8,
                             relheight=.1,
                             relwidth=.3,
                             anchor='center')


        self.correct_answer_img = Image.open("correct_answer_placeholder.jpg")
        self.correct_answer_img = self.correct_answer_img.resize((500,500,),Image.Resampling.LANCZOS)
        self.correct_answer_img2 = ImageTk.PhotoImage(self.correct_answer_img)
        self.correct_answer_label = tk.Label(
            self.canvas,
            image=self.correct_answer_img2,
            borderwidth=0
        )
        self.correct_answer_window = self.canvas.create_window(
            root.screen_width // 2,
            root.screen_height // 2,
            window=self.correct_answer_label,
            state="hidden"
        )
        self.answer_labels = [
            self.answer_1_label,
            self.answer_2_label,
            self.answer_3_label,
            self.answer_4_label
        ]
        for label in self.answer_labels:
            label.bind(
                "<Button-1>",
                lambda event, lbl=label:
                self.answer_checker(lbl)
            )
        self.incorrect_answer_img = Image.open("incorrect_answer_placeholder.jpg")
        self.incorrect_answer_img = self.incorrect_answer_img.resize((500,500,),Image.Resampling.LANCZOS)
        self.incorrect_answer_img2 = ImageTk.PhotoImage(self.incorrect_answer_img)
        self.incorrect_answer_label = tk.Label(
            self.canvas,
            image=self.incorrect_answer_img2,
            borderwidth=0
        )
        self.incorrect_answer_window = self.canvas.create_window(
            root.screen_width // 2,
            root.screen_height // 2,
            window=self.incorrect_answer_label,
            state="hidden"
        )

        self.time_limit_img = Image.open("yttlcover.jpg")
        self.time_limit_img = self.time_limit_img.resize((500,500,),Image.Resampling.LANCZOS)
        self.time_limit_img2 = ImageTk.PhotoImage(self.time_limit_img)
        self.time_limit_label = tk.Label(
            self.canvas,
            image=self.time_limit_img2,
            borderwidth=0
        )
        self.time_limit_window = self.canvas.create_window(
            root.screen_width // 2,
            root.screen_height // 2,
            window=self.time_limit_label,
            state="hidden"
        )

        if self.timeout_status is not True:
            self.canvas.after_cancel(self.timeout_status)
            self.timeout_status = True

        
        self.frame_window = self.canvas.create_window(
            root.screen_width // 2,
            root.screen_height // 2,
            window=self.multiple_choice_questions_frame,
            width=int(root.screen_width * 0.8),
            height=int(root.screen_height * 0.7),
            anchor="center",
            state="hidden"
        )

    def time_limit(self):
        self.canvas.itemconfigure(self.time_limit_window, state="normal")

        self.canvas.after(
            1000,
            lambda: (
                self.canvas.itemconfigure(self.time_limit_window, state="hidden"),
                self.canvas.itemconfigure(self.frame_window, state="hidden")
            )
        )
    def create_question(self):
        self.question_generator()

        self.canvas.itemconfigure(
            self.frame_window,
            state="normal"
        )

        self.canvas.tag_raise(
            self.frame_window
        )

        if self.timeout_status is not True:
            self.canvas.after_cancel(
                self.timeout_status
            )

        self.timeout_status = self.canvas.after(
            2000,
            lambda: self.time_limit()
        )
