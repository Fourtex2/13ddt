import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = tk.Tk()
root.title("window")

screen_width = int(root.winfo_screenwidth())
screen_height = int(root.winfo_screenheight())
x = (screen_width - screen_width) // 2
y = (screen_height - screen_height) // 2

root.geometry(f"{screen_width}x{screen_height}+{x}+{y}")
root.maxsize(screen_width,screen_height)
root.minsize(int(screen_width/1.5),int(screen_height/1.8))


background = Image.open("13ddt_assets_dump_ddt_menu_background_autosave copy.png")
background = background.resize(
    (
        screen_width,
        screen_height
        )
    )
background2 = ImageTk.PhotoImage(background)
backgroundlabel = tk.Label(image=background2)
backgroundlabel.place(relx=0.5, rely=0.5, anchor="center")
backgroundlabel.lower()

loginframe = tk.Frame(
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

nextpageframe = tk.Frame(bg='blue')

incorrect_login_label = tk.Label(
    text="INCORRECT USERNAME OR PASSWORD",bg='grey'
)







closewindowframe = tk.Frame(bg='red')
closewindowframe.place(relx=.5,rely=0.9,relwidth=.1,relheight=.1,anchor='center')
def close():
    root.destroy()
closebutton = tk.Button(closewindowframe, text="close", command=close)
closebutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')

# icon = ImageTk.PhotoImage(Image.open("window_icon_placeholder.png"))
# root.iconbitmap(icon)
root.mainloop()
