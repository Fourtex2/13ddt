import tkinter as tk
import random

root = tk.Tk()

screen_width = int(root.winfo_screenwidth() / 1.3)
screen_height = int(root.winfo_screenheight() / 1.5)

root.geometry(f"{screen_width}x{screen_height}")
root.resizable(False, False)

question_label = tk.Label(root)
question_label.place(relx=0.5, rely=0.4, anchor="center")

x_label = tk.Label(root)
x_label.place(relx=0.5, rely=0.45, anchor="center")

answer_label = tk.Label(root)
answer_label.place(relx=0.5, rely=0.5, anchor="center")


global random_number

random_number = list(range(1, 100))
random.shuffle(random_number)

def create_new_question():
    random.shuffle(random_number)

    random_x_value = random_number[random.randint(1,98)]
    random_number_1 = random_number[random.randint(1,98)]
    random_number_2 = random_number[random.randint(1,98)]
    random_number_3 = random_number[random.randint(1,98)]
    random_number_4 = random_number[random.randint(1,98)]
    random_number_5 = random_number[random.randint(1,98)]
    random_number_6 = random_number[random.randint(1,98)]

    question_label.config(text=f"X × {random_number_1} x {random_number_2}")
    answer_label.config(text=random_x_value * random_number_1 * random_number_2)
    x_label.config(text=f"x = {random_x_value}")

newquestion = tk.Button(root, text="New Question", command=create_new_question)
newquestion.place(relx=0.5, rely=0.2, anchor="center")

create_new_question()  # Show the first question immediately

root.mainloop()