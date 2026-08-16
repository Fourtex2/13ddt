import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from database import *

class loginscreen(tk.Frame):
    def __init__(self, screen, root):
        tk.Frame.__init__(self, screen)
        self.root = root
        self.background = Image.open(
            "placeholder_background.png"
            )
        self.background = self.background.resize(
            (
                root.screen_width,
                root.screen_height
                )
            )
        self.background2 = ImageTk.PhotoImage(self.background)
        self.backgroundlabel = tk.Label(self,image=self.background2)
        self.backgroundlabel.place(relx=0.5, rely=0.5, anchor="center")
        self.backgroundlabel.lower()

        loginframe = tk.Frame(
            self,
            bg="lightblue"
        )
        loginframe.place(
            relx=0.5,
            rely=0.6,
            relwidth=.3,
            relheight=.15,
            anchor='center'
            )
        username_label = tk.Label(
            loginframe,
            text="ENTER USERNAME"
            )
        
        username_label.place(relx=.25,rely=.3,relwidth=.4,relheight=.13, anchor='center')
        username_entry = tk.Entry(loginframe)

        username_entry.place(relx=.6,rely=.3,relwidth=.4,relheight=.13, anchor='center')
        password_label = tk.Label(loginframe, text="password")

        password_label.place(relx=.25,rely=.5,relwidth=.4,relheight=.13, anchor='center')
        password_entry = tk.Entry(loginframe)
        
        password_entry.place(relx=.6,rely=.5,relwidth=.4,relheight=.13, anchor='center')

        nextpageframe = tk.Frame(self,bg='blue')
        def login(self):
            load_user()

            from title import titlescreen
            root.show_frame(titlescreen)
        nextpageframe.place(relx=.5,rely=0.8,relwidth=.1,relheight=.1,anchor='center')
        nextpagebutton = tk.Button(nextpageframe, text="next page", command=login)
        nextpagebutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')


        closewindowframe = tk.Frame(self,bg='red')
        closewindowframe.place(relx=.5,rely=0.9,relwidth=.1,relheight=.1,anchor='center')
        def close():
            root.destroy()
        closebutton = tk.Button(closewindowframe, text="close", command=close)
        closebutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')

        # icon = ImageTk.PhotoImage(Image.open("window_icon_placeholder.png"))
        # root.iconbitmap(icon)
