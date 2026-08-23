import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import random
import achieved_multiple_choice
import login

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

        
        self.background = Image.open("13ddt_assets_dump_ddt_menu_background_autosave copy.png")
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

        self.progressbar_frame = Image.open("progress_bar_placeholder.png")
        self.progressbar_frame = self.progressbar_frame.resize(
            (
                root.screen_width,
                int(root.screen_height * 0.7)
            ),
            Image.Resampling.LANCZOS
        )
        self.progressbar2 = ImageTk.PhotoImage(self.progressbar_frame)

        self.progressbar_frame_window = self.create_image(
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

        self.progressbar_bar_window2 = self.create_image(
            int(root.screen_width * -0.2),
            int(root.screen_height * -0.03),
            image=self.progressbar_bar2,
            anchor='center'
        )
        
        self.achieved_questions_file.bar_mover()

        self.tag_raise(self.progressbar_frame_window)

        achieved_button_img = Image.open(
            "new_question.png"
        )
        achieved_button_img = achieved_button_img.resize(
            (500, 350),
            Image.Resampling.LANCZOS
        )
        self.button_test_image = ImageTk.PhotoImage(
            achieved_button_img
        )

        self.multiple_choice_button_window = self.create_image(
            root.screen_width * 0.5,
            root.screen_height * 0.6,
            image=self.button_test_image,
            anchor = 'center',
            state = "normal"
        )

        def button_clicked(event):
            self.achieved_questions_file.create_question()

        self.tag_bind(
            self.multiple_choice_button_window,
            "<Button-1>",
            button_clicked
        )