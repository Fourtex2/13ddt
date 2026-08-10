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
        self.achieved_questions_file = (
            achieved_multiple_choice.AchievedQuestions(
                self,
                root
            )
        )
        self.background = Image.open("placeholder_background.png")
        self.background = self.background.resize(
            (root.screen_width, root.screen_height)
        )
        self.background2 = ImageTk.PhotoImage(self.background)

        self.background_item = self.create_image(
            int(root.screen_width // 2),
            int(root.screen_height // 2),
            image=self.background2,
            anchor="center"
        )

        self.progressbar = Image.open("progress_bar_placeholder.png")
        self.progressbar = self.progressbar.resize(
            (
                root.screen_width,
                int(root.screen_height * 0.7)
            ),
            Image.Resampling.LANCZOS
        )
        self.progressbar2 = ImageTk.PhotoImage(self.progressbar)

        self.progressbar_item1 = self.create_image(
            int(root.screen_width // 2),
            int(root.screen_height * 0.3),
            image=self.progressbar2,
            anchor="center"
        )

        self.progressbar_bar = Image.open(
            "progress_bar_bar_placeholder.png"
        )
        self.progressbar_bar = self.progressbar_bar.resize(
            (
                int(root.screen_width * 1.2),
                int(root.screen_height * 1.4)
            ),
            Image.Resampling.LANCZOS
        )
        self.progressbar_bar2 = ImageTk.PhotoImage(
            self.progressbar_bar
        )

        self.progressbar_bar_item2 = self.create_image(
            int(root.screen_width * -0.45 * self.achieved_questions_file.energy_amount),
            int(root.screen_height * -0.03),
            image=self.progressbar_bar2,
            anchor='center'
        )

        self.tag_raise(self.progressbar_item1)

        achieved_button_img = Image.open(
            "button_achieveed_questions_placeholder.png"
        )
        achieved_button_img = achieved_button_img.resize(
            (200, 120),
            Image.Resampling.LANCZOS
        )

        self.button_test_image = ImageTk.PhotoImage(
            achieved_button_img
        )

        self.multiple_choice_button = tk.Label(
            self,
            image=self.button_test_image,
            borderwidth=0,
            highlightthickness=0
        )

        self.create_window(
            root.screen_width * 0.2,
            root.screen_height * 0.7,
            window=self.multiple_choice_button
        )



        def button_clicked(event):
            print("ibhjn")
            self.achieved_questions_file.create_question()

        self.multiple_choice_button.bind(
            "<Button-1>",
            button_clicked
        )
        
        self.tag_raise(
        self.achieved_questions_file.correct_answer_window
        )

        self.tag_raise(
            self.achieved_questions_file.incorrect_answer_window
        )

        self.tag_raise(
            self.achieved_questions_file.time_limit_window
        )

        self.tag_raise(
            self.achieved_questions_file.frame_window
        )