import tkinter as tk
from PIL import Image, ImageTk
import random
import questions
import tkinter.font as tkFont

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

    def bar_mover(self):
        start_x = int(self.root.screen_width * -0.45)
        start_y = int(self.root.screen_height * -0.03)

        movement = int(
            self.root.screen_width * 0.01 * self.energy_amount
        )

        self.canvas.coords(
            self.canvas.progressbar_bar_window2,
            start_x + movement,
            start_y
        )

    def answer_checker(self, clicked_label):

        if self.timeout_status is not None:
            self.canvas.after_cancel(self.timeout_status)
            self.timeout_status = None

        if self.answer_image_status is not None:
            self.canvas.after_cancel(self.answer_image_status)
            self.answer_image_status = None

        self.hide_question_labels()

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
            self.canvas.tag_raise(
                self.canvas.multiple_choice_button_window
            )
            self.answer_image_status = self.canvas.after(
                1000,
                self.hide_answer_image
            )
            self.canvas.tag_lower(
                self.question_background_window
            )
            self.canvas.itemconfigure(
                self.question_background_window,
                state="hidden"
            )

            self.bar_mover()
            self.correct_answers_answered += 1

        else:

            self.energy_amount -= 4989898398239823983298
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
            self.canvas.tag_raise(
                self.canvas.multiple_choice_button_window
            )
            self.answer_image_status = self.canvas.after(
                1000,
                self.hide_answer_image
            )
            self.canvas.tag_lower(
                self.question_background_window
            )
            self.canvas.itemconfigure(
                self.question_background_window,
                state="hidden"
            )

            self.bar_mover()
            if self.energy_amount <= 0:
                self.game_over()
            self.incorrect_answers_answered += 1


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
    def hide_question_labels(self):
        self.question_label.place_forget()
        self.answer_1_label.place_forget()
        self.answer_2_label.place_forget()
        self.answer_3_label.place_forget()
        self.answer_4_label.place_forget()
        
    def show_questions(self):
        self.canvas.itemconfigure(
            self.question_background_window,
            state="normal"
        )
        self.canvas.tag_raise(
            self.question_background_window
        )
        self.canvas.tag_lower(
            self.canvas.multiple_choice_button_window
        )
        self.question_label.place(
            relx=.5,
            rely=.35,
            relheight=.1,
            relwidth=.7,
            anchor="center"
        )
        self.answer_1_label.place(
            relx=.3,
            rely=.5,
            relheight=.1,
            relwidth=.3,
            anchor='center')
        self.answer_2_label.place(
            relx=.7,
            rely=.5,
            relheight=.1,
            relwidth=.3,
            anchor='center')
        self.answer_3_label.place(
            relx=.3,
            rely=.7,
            relheight=.1,
            relwidth=.3,
            anchor='center')
        self.answer_4_label.place(
            relx=.7,
            rely=.7,
            relheight=.1,
            relwidth=.3,
            anchor='center')
        
    def game_over(self):
        self.canvas.itemconfigure(
            self.question_background_window,
            state = "normal"
        )
        self.canvas.itemconfigure(
            self.canvas.multiple_choice_button_window,
            state = "hidden"
        )
        self.canvas.tag_raise(
            self.question_background_window
        )        
        self.canvas.lower(
            self.canvas.multiple_choice_button_window
        )

        self.canvas.itemconfigure(
            self.game_over_title2,
            state = "normal"
        )
        self.total_score.place(
            relx=.5,
            rely=.5,
            relheight=.2,
            relwidth=.7,
            anchor="center"
        )
        print("GAME OVER")

        

    def __init__(self, canvas, root):
        self.correct_answers_answered = 0
        self.incorrect_answers_answered = 0
        self.canvas = canvas
        self.root = root
        self.energy_amount = 10
        self.answer_image_status = None
        self.timeout_status = None
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

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
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

        self.game_over_title = Image.open(
            "testimg.png"
        )
        self.game_over_title = self.game_over_title.resize(
            (
            int(root.screen_width * 0.8),
            int(root.screen_height * 0.7)),
            Image.Resampling.NEAREST
        )
        self.game_over_title2 = ImageTk.PhotoImage(
            self.game_over_title
        ) 
        self.game_over_title_window = self.canvas.create_image(
            root.screen_width // 2,
            root.screen_height // 2,
            image=self.game_over_title2,
            anchor="center",
            state="hidden"
        )




#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------

        self.question_background = Image.open(
            "ddt_questions_plate.001.png"
        )
        self.question_background = self.question_background.resize(
            (
            int(root.screen_width * 0.8),
            int(root.screen_height * 0.7)),
            Image.Resampling.NEAREST
        )
        self.question_background2 = ImageTk.PhotoImage(
            self.question_background
        )
        self.question_background_window = self.canvas.create_image(
            root.screen_width // 2,
            root.screen_height // 2,
            image=self.question_background2,
            anchor="center",
            state="hidden"
        )
            
        # self.multiple_choice_questions_background = tk.Frame(self.canvas,bg="grey")
        
        # self.question_background_window = self.canvas.create_window(
        #     root.screen_width // 2,
        #     root.screen_height // 2,
        #     window=self.multiple_choice_questions_background,
        #     width=int(root.screen_width * 0.8),
        #     height=int(root.screen_height * 0.7),
        #     anchor="center",
        #     state="hidden"
        # )

        self.Courier = tkFont.Font(family="Courier")


        self.question_label = tk.Label(self.canvas,
                                       bg="blue",
                                       font=self.Courier)

        self.answer_1_label = tk.Label(self.canvas,
                                       bg="green",
                                       font=self.Courier)
        self.answer_2_label = tk.Label(self.canvas,
                                       bg="green",
                                       font=self.Courier)
        self.answer_3_label = tk.Label(self.canvas,
                                       bg="green",
                                       font=self.Courier)
        self.answer_4_label = tk.Label(self.canvas,
                                       bg="green",
                                       font=self.Courier)
        
        self.total_score = tk.Label(self.canvas,
                        bg="red",
                        font=self.Courier,
                        text=self.correct_answers_answered)
        self.correct_answer_img = Image.open(
            "ddt_correct.png"
        )
        self.correct_answer_img = self.correct_answer_img.resize(
            (root.screen_width, root.screen_height),
            Image.Resampling.NEAREST
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
            "ddt_incorrect.png"
        )
        self.incorrect_answer_img = self.incorrect_answer_img.resize(
            (root.screen_width, root.screen_height),
            Image.Resampling.NEAREST
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

        self.time_limit_img = Image.open(
            "yttlcover.jpg"
        )
        self.time_limit_img = self.time_limit_img.resize(
            (500, 500),
            Image.Resampling.NEAREST
        )
        self.time_limit_img2 = ImageTk.PhotoImage(self.time_limit_img)
        self.time_limit_window = self.canvas.create_image(
            root.screen_width // 2,
            root.screen_height // 2,
            image=self.time_limit_img2,
            anchor="center",
            state="hidden"
            )


        
    def time_limit(self):

        self.timeout_status = None
        self.energy_amount -= 3

        if self.answer_image_status is not None:
            self.canvas.after_cancel(
                self.answer_image_status
            )
            self.answer_image_status = None

        self.canvas.itemconfigure(
            self.question_background_window,
            state="hidden"
        )

        self.hide_question_labels()

        self.canvas.itemconfigure(
            self.correct_answer_window,
            state="hidden"
        )

        self.canvas.itemconfigure(
            self.incorrect_answer_window,
            state="hidden"
        )

        self.canvas.itemconfigure(
            self.time_limit_window,
            state="normal"
        )

        self.canvas.tag_raise(
            self.time_limit_window
        )

        self.canvas.tag_lower(
            self.question_background_window
        )
        self.canvas.itemconfigure(
            self.question_background_window,
            state="hidden"
        )

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

        self.show_questions()

        if self.timeout_status is not None:
            self.canvas.after_cancel(
                self.timeout_status
            )
            self.timeout_status = None

        self.timeout_status = self.canvas.after(
            2000,
            self.time_limit
        )