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

icon = ImageTk.PhotoImage(Image.open("window_icon_placeholder.png"))
root.iconbitmap(icon)

img = Image.open("placeholder_background.png")
img = img.resize((screen_width,screen_height))
img2 = ImageTk.PhotoImage(img)
imglabel = tk.Label(root,image=img2)
imglabel.place(relx=0.5, rely=0.5, anchor="center")
imglabel.lower()

login = tk.Frame(root, bg="lightblue")
login.place(relx=0.5,rely=0.2,relwidth=.3,relheight=.15,anchor='center')

username_label = tk.Label(login, text="ENTER USERNAME")
username_label.place(relx=.25,rely=.3,relwidth=.4,relheight=.13, anchor='center')
username_entry = tk.Entry(login)
username_entry.place(relx=.6,rely=.3,relwidth=.4,relheight=.13, anchor='center')
password_label = tk.Label(login, text="password")
password_label.place(relx=.25,rely=.5,relwidth=.4,relheight=.13, anchor='center')
password_entry = tk.Entry(login)
password_entry.place(relx=.6,rely=.5,relwidth=.4,relheight=.13, anchor='center')

combobox_frame = tk.Frame(root, bg="lightblue")
combobox_frame.place(relx=.5,rely=0.35,relwidth=.4,relheight=.1,anchor='center')
combobox_items = ["a","b","c"]
combobox = ttk.Combobox(combobox_frame, values=combobox_items)
combobox.set("combobox")
combobox.place(relx=.5,rely=.5,relheight=.6,relwidth=.6,anchor='center')

radiobutton_frame = tk.Frame(root,bg='lightblue')
radiobutton_frame.place(relx=.5,rely=0.55,relwidth=.4,relheight=.2,anchor='center')
radiobutton_default = str("a")
for i, button in enumerate(["a","b","c"]):
    Radiobutton(radiobutton_frame, text=button, variable=radiobutton_default, value=button).place(relx=.5,rely=.2 + i * .2,relheight=.15,relwidth=.3,anchor='center')

checkbuttonframe = tk.Frame(root,bg='lightblue')
checkbuttonframe.place(relx=.5,rely=0.75,relwidth=.4,relheight=.1,anchor='center')

Checkbuttonnumber = tk.IntVar #makes a integer variable
Checkbutton = tk.Checkbutton(checkbuttonframe,text="checkbutton", variable=Checkbuttonnumber,onvalue=1, offvalue=0) #on/off value is dependant on the interger value which changes when pressed
Checkbutton.config(bg='darkblue')
Checkbutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')

closewindowframe = tk.Frame(root,bg='red')
closewindowframe.place(relx=.5,rely=0.9,relwidth=.1,relheight=.1,anchor='center')
def close():
    root.destroy()
closebutton = tk.Button(closewindowframe, text="close", command=close)
closebutton.place(relx=.5,rely=0.55,relwidth=.4,relheight=.5,anchor='center')

root.mainloop()

