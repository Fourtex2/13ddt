import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

from login import loginscreen
from maingame import game

class root(tk.Tk):
    def __init__(self,*args, **kwargs): #*args and **kwargs allows any number of arguements to be passed through
        tk.Tk.__init__(self, *args, **kwargs)

        screen = tk.Frame(self)
        self.title("window")

        self.screen_width = int(self.winfo_screenwidth())
        self.screen_height = int(self.winfo_screenheight())
        print(self.screen_width)
        print(self.screen_height)
        x = (self.screen_width - self.screen_width) // 2
        y = (self.screen_height - self.screen_height) // 2

        self.geometry(f"{self.screen_width}x{self.screen_height}+{x}+{y}")
        self.maxsize(self.screen_width,self.screen_height)
        self.minsize(int(self.screen_width/1.5),int(self.screen_height/1.8))
        
        self.currentscreen = {} #creates empty dictionary where the current frame is being stored

        screen.place(relwidth=1, relheight  =1)

        for loadedframe in (loginscreen,game): #loaded frame is the current screen being shown
            frame = loadedframe(screen,self) #frame is the loaded frame, and makes a object
            self.currentscreen[loadedframe] = frame
            frame.place(relwidth=1, relheight=1)
        
        self.show_frame(loginscreen)
        
    def show_frame(self, currentframe):
        frame = self.currentscreen[currentframe]
        frame.tkraise()

app = root()
app.mainloop()
