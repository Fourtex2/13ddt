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

root.geometry('500x700')
root['bg'] = "#DCDCDC"

titleframe = tk.Frame(root,bg="#162D86")
titleframe.place(relx=.5,rely=0,relwidth=1,relheight=.4,anchor='center')

title = tk.Label(titleframe, text="MACLEANS COLLEGE", bg="#162D86", fg="gold")
title.place(relx=.6,rely=.75,relwidth=1,relheight=.4,anchor='center')
title.config(font=("Arial",25))


img = Image.open("macleans.png")
img = img.resize((20,20))
img2 = ImageTk.PhotoImage(img)
imglabel = tk.Label(titleframe,image=img2)
imglabel.place(relx=0.1, rely=0.1, anchor="center")



studentdetails = tk.Frame(root,bg="#FFFFFF")
studentdetails.place(relx=.5,rely=.45,relwidth=.9,relheight=.4,anchor='center')
detaillabel = tk.Label(studentdetails, text="Student Details",bg="white",fg="Blue")
detaillabel.config(font=("Arial",25))
detaillabel.place(relx=.5, rely=.1, relwidth=.9, relheight=.3, anchor='center')

name_label = tk.Label(studentdetails, text="Name",bg="white",fg="Blue")
name_label.place(relx=.1,rely=.3,relwidth=.4,relheight=.13, anchor='center')
name_label.config(font=("Arial",15))

name_entry = tk.Entry(studentdetails,bg="lightGrey",fg="Black")
name_entry.place(relx=.5,rely=.3,relwidth=.6,relheight=.09, anchor='center')

Date_label = tk.Label(studentdetails, text="Date",bg="white",fg="Blue")
Date_label.place(relx=.1,rely=.5,relwidth=.4,relheight=.13, anchor='center')
Date_label.config(font=("Arial",15))

Date_entry = tk.Entry(studentdetails,bg="LightGrey",fg="Black")
Date_entry.place(relx=.5,rely=.5,relwidth=.6,relheight=.09, anchor='center')

Time_label = tk.Label(studentdetails, text="Name",bg="white",fg="Blue")
Time_label.place(relx=.1,rely=.7,relwidth=.4,relheight=.13, anchor='center')
Time_label.config(font=("Arial",15))

Time_entry = tk.Entry(studentdetails,bg="lightGrey",fg="Black")
Time_entry.place(relx=.5,rely=.7,relwidth=.6,relheight=.09, anchor='center')

House_label = tk.Label(studentdetails, text="House",bg="white",fg="Blue")
House_label.place(relx=.1,rely=.9,relwidth=.4,relheight=.13, anchor='center')
House_label.config(font=("Arial",15))

Houses = ["Rutherford",
          "Te Kanawa",
          "Batten",
          "Mansfield",
          "Kupe",
          "Hillary",
          "Upham",
          "Snell"]
Housecombobox = ttk.Combobox(studentdetails, values=Houses)
Housecombobox.place(relx=.5,rely=.9,relwidth=.6,relheight=.13, anchor='center')

def submit():
    print(Time_entry)
Submitbutton = tk.Button(root,text="Submit Check-In",command=submit)
Submitbutton.place(relx=.5,rely=.72,relwidth=.35,relheight=.08, anchor='center')

Quotebg = tk.Label(root, bg="#162D86")
Quotebg.place(relx=.5,rely=1,relwidth=1,relheight=.4,anchor='center')

listofquotes = ["quote 1"
                "quote 2"
                "quote 3"]
quote = tk.Label(Quotebg,bg="#162D86",fg="Black",text=listofquotes[0])
quote.place(relx=.5,rely=.1,relwidth=1,relheight=.4,anchor='center')

def newquote():
    i = 0
    while i < len(listofquotes):
        quote = listofquotes[i]
        i = i + 1
quotebutton = tk.Button(Quotebg,text="New quote", bg="#162D86",fg="Black",command=newquote)
quotebutton.place(relx=.5,rely=.3,relwidth=.4,relheight=.2,anchor='center')



root.mainloop()

