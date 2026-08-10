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
        if self.timeout_status is not None:
            self.canvas.after_cancel(self.timeout_status)
            self.timeout_status = None

        if self.answer_image_status is not None:
            self.canvas.after_cancel(self.answer_image_status)
            self.answer_image_status = None

        self.canvas.itemconfigure(
            self.frame_window,
            state="hidden"
        )

        if clicked_label == self.answer_labels[self.correct_answer]:

            self.energy_amount += 6
            print(self.energy_amount)

            self.canvas.itemconfigure(
                self.incorrect_answer_window,
                state="hidden"
            )

            self.canvas.itemconfigure(
                self.correct_answer_window,
                state="normal"
            )

            self.canvas.tag_raise(
                self.correct_answer_window
            )


            self.answer_image_status = self.canvas.after(
                1000,
                self.hide_answer_image
            )

        else:
            self.energy_amount -= 4
            print(self.energy_amount)

            self.canvas.itemconfigure(
                self.correct_answer_window,
                state="hidden"
            )

            self.canvas.itemconfigure(
                self.incorrect_answer_window,
                state="normal"
            )

            self.canvas.tag_raise(
                self.incorrect_answer_window
            )


            self.answer_image_status = self.canvas.after(
                1000,
                self.hide_answer_image
            )

    def hide_answer_image(self):

        self.canvas.itemconfigure(
            self.correct_answer_window,
            state="hidden"
        )

        self.canvas.itemconfigure(
            self.incorrect_answer_window,
            state="hidden"
        )

        self.answer_image_status = None

    def __init__(self, canvas, root):

        self.canvas = canvas
        self.root = root
        self.energy_amount = 0
        self.answer_image_status = None
        self.timeout_status = None

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

        self.correct_answer_img = Image.open(
            "correct_answer_placeholder.jpg"
        )

        self.correct_answer_img = self.correct_answer_img.resize(
            (500, 500),
            Image.Resampling.LANCZOS
        )

        self.correct_answer_img2 = ImageTk.PhotoImage(
            self.correct_answer_img
        )

        self.correct_answer_window = self.canvas.create_image(
            root.screen_width // 2,
            root.screen_height // 2,
            image=self.correct_answer_img2,
            anchor="center",
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
            
        self.incorrect_answer_img = Image.open(
            "incorrect_answer_placeholder.jpg"
        )

        self.incorrect_answer_img = self.incorrect_answer_img.resize(
            (500, 500),
            Image.Resampling.LANCZOS
        )

        self.incorrect_answer_img2 = ImageTk.PhotoImage(
            self.incorrect_answer_img
        )

        self.incorrect_answer_window = self.canvas.create_image(
            root.screen_width // 2,
            root.screen_height // 2,
            image=self.incorrect_answer_img2,
            anchor="center",
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

        self.timeout_status = None

        # Cancel result image timer if one exists
        if self.answer_image_status is not None:
            self.canvas.after_cancel(
                self.answer_image_status
            )
            self.answer_image_status = None

        # Hide question
        self.canvas.itemconfigure(
            self.frame_window,
            state="hidden"
        )

        # Hide result images
        self.canvas.itemconfigure(
            self.correct_answer_window,
            state="hidden"
        )

        self.canvas.itemconfigure(
            self.incorrect_answer_window,
            state="hidden"
        )

        # Show timeout
        self.canvas.itemconfigure(
            self.time_limit_window,
            state="normal"
        )

        self.canvas.tag_raise(
            self.time_limit_window
        )

        self.time_limit_label.lift()

        self.canvas.after(
            1000,
            lambda: self.canvas.itemconfigure(
                self.time_limit_window,
                state="hidden"
            )
        )
    def create_question(self):

        if self.answer_image_status is not None:
            self.canvas.after_cancel(
                self.answer_image_status
            )
            self.answer_image_status = None

        self.canvas.itemconfigure(
            self.correct_answer_window,
            state="hidden"
        )

        self.canvas.itemconfigure(
            self.incorrect_answer_window,
            state="hidden"
        )

        self.question_generator()

        self.canvas.itemconfigure(
            self.frame_window,
            state="normal"
        )

        self.multiple_choice_questions_frame.update_idletasks()

        self.canvas.tag_raise(
            self.frame_window
        )

        if self.timeout_status is not None:
            self.canvas.after_cancel(
                self.timeout_status
            )
            self.timeout_status = None

        self.timeout_status = self.canvas.after(
            2000,
            self.time_limit
        )