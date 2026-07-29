import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class game(tk.Frame):
    def __init__(self, screen, root):
        super().__init__(screen)

        self.reactorcanvas = reactor(self, root)
        self.reactorcanvas.place(relwidth=1, relheight=1,relx=.5,rely=.5,anchor='center')

class reactor(tk.Canvas):
    def __init__(self, screen, root):
        super().__init__(screen)
        reactor.config(self , bg="green")

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
        self.progressbar = self.progressbar.resize((root.screen_width, int(root.screen_height * 0.7)), Image.Resampling.LANCZOS)
        self.progressbar2 = ImageTk.PhotoImage(self.progressbar)

        self.create_image(
            int(root.screen_width // 2),
            int(root.screen_height * 0.3),
            image=self.progressbar2,
            anchor="center"
        )

        def multiple_choice_questions():
            if multiple_choice_questions_frame.winfo_ismapped():
                multiple_choice_questions_frame.place_forget()
            else:
                multiple_choice_questions_frame.place(relx=.5,rely=0.5,relwidth=.8,relheight=.9,anchor='center')
        multiple_choice_questions_frame = tk.Frame(self,bg="green")
        multiple_choice_question_label = tk.Label(multiple_choice_questions_frame,bg="white",text="TEST")
        multiple_choice_question_label.place(relx=.5,rely=.2,relheight=.1,relwidth=.7,anchor='center')
        multiple_choice_button = tk.Button(self,command=multiple_choice_questions)
        multiple_choice_button.place(relx=.25,rely=0.8,relwidth=.2,relheight=.2,anchor='center')