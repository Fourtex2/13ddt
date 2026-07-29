import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class titlescreen(tk.Frame):
    def __init__(self, screen, root):
        tk.Frame.__init__(self, screen)
        self.background = Image.open("placeholder_background_title.png")
        self.background = self.background.resize((root.screen_width,root.screen_height))
        self.background2 = ImageTk.PhotoImage(self.background)
        self.backgroundlabel = tk.Label(self,image=self.background2)
        self.backgroundlabel.place(relx=0.5, rely=0.5, anchor="center")
        self.backgroundlabel.lower()


        self.title = Image.open("Placeholder_title.png")
        self.title = self.title.resize((int(root.screen_width/2),int(root.screen_height/3)))
        self.title2 = ImageTk.PhotoImage(self.title)
        self.title_label = tk.Label(self, image=self.title2)
        self.title_label.place(relx=.5, rely=.2, anchor='center')
        self.title_label.tkraise()

        def loadmaingame():
            from maingame import game
            root.show_frame(game)
        playbutton = tk.Button(self,bg="pink",text="play", command=loadmaingame)
        playbutton.place(relx=.5,rely=0.5,relwidth=.2,relheight=.15,anchor='center')

        def TEST():
            if setingsframe.winfo_ismapped():
                setingsframe.place_forget()
            else:
                setingsframe.place(relx=.5,rely=0.6,relwidth=.4,relheight=.4,anchor='center')

        setingsframe = tk.Frame(self, bg="lightgreen")
        settingsbutton = tk.Button(self, text = "settings", command=TEST)
        settingsbutton.place(relx=.5,rely=0.7,relwidth=.15,relheight=.1,anchor='center')


        closewindowframe = tk.Frame(self,bg='red')
        closewindowframe.place(relx=.5,rely=0.9,relwidth=.1,relheight=.1,anchor='center')
        def close():
            root.destroy()
        closebutton = tk.Button(closewindowframe, text="close", command=close)
        closebutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')
