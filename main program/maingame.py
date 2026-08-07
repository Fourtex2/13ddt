import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import sympy as sp
import re
import questions
import time
import achieved_multiple_choice

class game(tk.Frame):
    def __init__(self, screen, root):
        super().__init__(screen)

        self.reactorcanvas = reactor(self, root)
        self.reactorcanvas.place(relwidth=1, relheight=1,relx=.5,rely=.5,anchor='center')

class reactor(tk.Canvas):
    def __init__(self, screen, root):
        super().__init__(screen)

        self.background = Image.open("placeholder_background.png")
        self.background = self.background.resize((root.screen_width, root.screen_height))
        self.background2 = ImageTk.PhotoImage(self.background)

        self.create_image(
            int(root.screen_width // 2),
            int(root.screen_height // 2),
            image=self.background2,
            anchor='center'
        )

        self.progressbar = Image.open("progress_bar_placeholder.png")
        self.progressbar = self.progressbar.resize((root.screen_width,
                                                    int(root.screen_height * 0.7)),
                                                    Image.Resampling.LANCZOS)
        self.progressbar2 = ImageTk.PhotoImage(self.progressbar)

        self.create_image(
            int(root.screen_width // 2),
            int(root.screen_height * 0.3),
            image=self.progressbar2,
            anchor="center"
        )

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------


        # def time_limit():
        #     def show():
        #         self.itemconfigure(time_limit_window, state="normal")

        #         self.after(
        #             1000,
        #             lambda: (
        #                 self.itemconfigure(time_limit_window, state="hidden"),
        #                 self.itemconfigure(frame_window, state="hidden")
        #             )
        #         )
        #     show()     
        # def multiple_choice_questions():
        #     if self.itemcget(frame_window, "state") == "hidden":
        #         question_generator()
        #         self.itemconfigure(frame_window, state="normal")
        #         multiple_choice_questions_frame.update_idletasks()
        #     else:
        #         self.itemconfigure(frame_window, state="hidden")

        #     if self.timeout_id is not True:
        #         self.after_cancel(self.timeout_id)
        #     self.timeout_id = self.after(2000, time_limit)

        # multiple_choice_questions_frame = tk.Frame(self,bg="grey")
        
        # achieved_multiple_choice = [
        #     questions.complex_modulus_achieved,
        #     questions.complex_argument_achieved,
        #     questions.complex_division_achieved,
        #     questions.complex_quadratic_achieved,
        #     questions.differentiation_basic_achieved,
        #     questions.differentiation_chain_achieved,
        #     questions.complex_multiplication_achieved,
        #     questions.differentiation_product_achieved,
        #     questions.differentiation_quotient_achieved
        # ]

        # question_label = tk.Label(multiple_choice_questions_frame,bg="blue")
        # question_label.place(relx=.5,
        #                      rely=.2,
        #                      relheight=.1,
        #                      relwidth=.7,
        #                      anchor='center')

        # answer_1_label = tk.Label(multiple_choice_questions_frame,bg="green")
        # answer_1_label.place(relx=.3,
        #                      rely=.4,
        #                      relheight=.1,
        #                      relwidth=.3,
        #                      anchor='center')
        
        # answer_2_label = tk.Label(multiple_choice_questions_frame,bg="green")
        # answer_2_label.place(relx=.6,
        #                      rely=.4,
        #                      relheight=.1,
        #                      relwidth=.3,
        #                      anchor='center')
        # answer_3_label = tk.Label(multiple_choice_questions_frame,bg="green")
        # answer_3_label.place(relx=.3,
        #                      rely=.8,
        #                      relheight=.1,
        #                      relwidth=.3,
        #                      anchor='center')
        # answer_4_label = tk.Label(multiple_choice_questions_frame,bg="green")
        # answer_4_label.place(relx=.6,
        #                      rely=.8,
        #                      relheight=.1,
        #                      relwidth=.3,
        #                      anchor='center')
        # self.timeout_id = True

        # def question_generator():
        #     question, answer = random.choice(achieved_multiple_choice)()

        #     false_answers = []

        #     while len(false_answers) < 3:
        #         bjwhdei, wrong = random.choice(achieved_multiple_choice)()

        #         if wrong != answer and wrong not in false_answers:
        #             false_answers.append(wrong)

        #     answer_list = [answer] + false_answers

        #     random.shuffle(answer_list)

        #     question_label.config(text=questions.format_fixer(question))
        #     answer_1_label.config(text=questions.format_fixer(answer_list[0]))
        #     answer_2_label.config(text=questions.format_fixer(answer_list[1]))
        #     answer_3_label.config(text=questions.format_fixer(answer_list[2]))
        #     answer_4_label.config(text=questions.format_fixer(answer_list[3]))
        #     global answer_labels
        #     answer_labels = [
        #         answer_1_label,
        #         answer_2_label,
        #         answer_3_label,
        #         answer_4_label
        #     ]
        #     global correct_answer
        #     correct_answer = answer_list.index(answer)

        #     for label in answer_labels:
        #         label.config(bg="red")
        #     answer_labels[correct_answer].config(bg="green")
        #     return answer_labels, correct_answer
        
        # answer_1_label.bind(
        #     "<Button-1>",
        #     lambda event: answer_checker(answer_1_label)
        # )

        # answer_2_label.bind(
        #     "<Button-1>",
        #     lambda event: answer_checker(answer_2_label)
        # )

        # answer_3_label.bind(
        #     "<Button-1>",
        #     lambda event: answer_checker(answer_3_label)
        # )

        # answer_4_label.bind(
        #     "<Button-1>",
        #     lambda event: answer_checker(answer_4_label)
        # )

        # correct_answer_img = Image.open("correct_answer_placeholder.jpg")
        # correct_answer_img = correct_answer_img.resize((500,500,),Image.Resampling.LANCZOS)
        # self.correct_answer_img2 = ImageTk.PhotoImage(correct_answer_img)
        # self.correct_answer_label = tk.Label(
        #     self,
        #     image=self.correct_answer_img2,
        #     borderwidth=0
        # )
        # correct_answer_window = self.create_window(
        #     root.screen_width // 2,
        #     root.screen_height // 2,
        #     window=self.correct_answer_label,
        #     state="hidden"
        # )

        # incorrect_answer_img = Image.open("incorrect_answer_placeholder.jpg")
        # incorrect_answer_img = incorrect_answer_img.resize((500,500,),Image.Resampling.LANCZOS)
        # self.incorrect_answer_img2 = ImageTk.PhotoImage(incorrect_answer_img)
        # self.incorrect_answer_label = tk.Label(
        #     self,
        #     image=self.incorrect_answer_img2,
        #     borderwidth=0
        # )
        # incorrect_answer_window = self.create_window(
        #     root.screen_width // 2,
        #     root.screen_height // 2,
        #     window=self.incorrect_answer_label,
        #     state="hidden"
        # )

        # time_limit_img = Image.open("yttlcover.jpg")
        # time_limit_img = time_limit_img.resize((500,500,),Image.Resampling.LANCZOS)
        # self.time_limit_img2 = ImageTk.PhotoImage(time_limit_img)
        # self.time_limit_label = tk.Label(
        #     self,
        #     image=self.time_limit_img2,
        #     borderwidth=0
        # )
        # time_limit_window = self.create_window(
        #     root.screen_width // 2,
        #     root.screen_height // 2,
        #     window=self.time_limit_label,
        #     state="hidden"
        # )

        # def answer_checker(clicked_label):
        #     if clicked_label == answer_labels[correct_answer]:
        #         self.itemconfigure(correct_answer_window, state="normal")
        #         self.tag_raise(correct_answer_window)
        #         self.after(#waits 1 sec
        #             1000,
        #             lambda: self.itemconfigure(correct_answer_window, state="hidden"))
        #     else:
        #         self.itemconfigure(incorrect_answer_window, state="normal")
        #         self.tag_raise(incorrect_answer_window)              
        #         self.after(#waits 1 sec
        #             1000,
        #             lambda: self.itemconfigure(incorrect_answer_window, state="hidden")
        #             )
        #     self.after(1500,
        #         lambda: self.itemconfigure(frame_window, state="hidden"))

        #     if self.timeout_id is not True:
        #         self.after_cancel(self.timeout_id)
        #         self.timeout_id = True
     
        # frame_window = self.create_window(
        #     root.screen_width // 2,
        #     root.screen_height // 2,
        #     window=multiple_choice_questions_frame,
        #     width=int(root.screen_width * 0.8),
        #     height=int(root.screen_height * 0.7),
        #     anchor="center",
        #     state="hidden"
        # )


#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------



        img = Image.open("button_achieveed_questions_placeholder.png")
        img = img.resize((200, 120), Image.Resampling.LANCZOS) 
        self.button_test_image = ImageTk.PhotoImage(img)
        self.multiple_choice_button = tk.Label(
            self,
            image=self.button_test_image,
            borderwidth=0,
            highlightthickness=0,
        )

        self.create_window(
            root.screen_width * 0.2,
            root.screen_height * 0.7,
            window=self.multiple_choice_button
        )

        self.questions_window = achieved_multiple_choice.AchievedQuestions(
            self,
            root
        )

        self.multiple_choice_button.bind(
            "<Button-1>",
            lambda event: self.questions_window.create_question(),
            print("ibhjn")
        )