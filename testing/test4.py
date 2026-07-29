import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

root.title("window")
root.geometry("670x670")

img = Image.open("testimg.png")
img = img.resize((650,650))

img2 = ImageTk.PhotoImage(img)

imglabel = tk.Label(root,image=img2).grid(row=3, column=0)
label = tk.Label(root, text="hello")
label.place(relx = 0.5, 
                   rely = 0.5,
                   anchor = 'center')

tk.Label(root,text="t1").grid(row=1, column=0)
tk.Label(root,text="t2").grid(row=1, column=0)

entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

entry1.grid(row=0, column=0)
entry2.grid(row=1, column=0)

root.mainloop()