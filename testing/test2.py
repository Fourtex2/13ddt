import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()



screen_width = int(root.winfo_screenwidth() / 1.3)
screen_height = int(root.winfo_screenheight() / 1.5)

root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, False)


img = Image.open("testimg.png")
img = img.resize((screen_width, screen_height))
img2 = ImageTk.PhotoImage(img)


imglabel = tk.Label(root, image=img2)
imglabel.place(x=0, y=0)

label = tk.Label(root, text="hello")
label.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()