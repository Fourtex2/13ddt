import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from database import *

class loginscreen(tk.Frame):
    def __init__(self, screen, root):
        create_tables()
        tk.Frame.__init__(self, screen)
        self.root = root
        self.background = Image.open("13ddt_assets_dump_ddt_menu_background_autosave copy.png")
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

        incorrect_login_label = tk.Label(
            root,text="INCORRECT USERNAME OR PASSWORD",bg='grey'
        )

        add_new_user_frame = tk.Frame(self, bg="blue")

        add_new_username_label = tk.Label(add_new_user_frame, text="username")
        add_new_username_label.place(relx =.5,rely=.1,relwidth=.7,relheight=.1,anchor='center')

        add_new_username_entry = tk.Entry(add_new_user_frame)
        add_new_username_entry.place(relx =.5,rely=.3,relwidth=.7,relheight=.1,anchor='center')

        add_new_password_label = tk.Label(add_new_user_frame, text="password")
        add_new_password_label.place(relx =.5,rely=.5,relwidth=.7,relheight=.1,anchor='center')

        add_new_password_entry = tk.Entry(add_new_user_frame)
        add_new_password_entry.place(
                                        relx =.5,
                                        rely=.7,
                                        relwidth=.7,
                                        relheight=.1,
                                        anchor='center'
                                    )

        close_new_user_button = tk.Button(add_new_user_frame,
                                          text="close",
                                          command=lambda:add_new_user_frame.place_forget())

        close_new_user_button.place(relx=.9,
                                    rely=.1,
                                    relheight=.1,
                                    relwidth=.1,
                                    anchor='center')

        def check_user():
            entered_new_username = add_new_username_entry.get()
            entered_new_password = add_new_password_entry.get()

            if entered_new_username == "" or entered_new_password == "":
                print("Please enter a username and password")
                return
            if len(entered_new_password) or len(entered_new_username) <= 25:
                print("Username or password too long")
                return

            if add_user(entered_new_username,
                        entered_new_password):
                print("Account created!")
                add_new_user_frame.place_forget()

            else:   
                print("Username already exists")

        submit_new_user_button = tk.Button(add_new_user_frame,text="Submit new user",command = check_user)
        submit_new_user_button.place(
                                    relx=.5,
                                    rely=.8,
                                    relheight=.1,
                                    relwidth=.2,
                                    anchor='center'
                                    )


        self.add_new_user_button = tk.Button(root,
                                        text="add new user",
                                        command=lambda:add_new_user_frame.place(
                                            relx=.5,
                                            rely=.42,
                                            relwidth=.4,
                                            relheight=.4,
                                            anchor='center'
                                        )
        )
        self.add_new_user_button.place(relx=.5,rely=0.7,relwidth=.1,relheight=.1,anchor='center')

        def login():
            entered_name = username_entry.get()
            entered_password = password_entry.get()

            if check_login(entered_name, entered_password):
                self.add_new_user_button.place_forget()
                from maingame import game
                root.show_frame(game)

            else:
                print("Incorrect username or password")
                incorrect_login_label.place(relx=.5,rely=.7,relheight=.1,relwidth=.2,anchor='center')
                incorrect_login_label.after(
                    1000,
                    incorrect_login_label.place_forget
                )

        
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
