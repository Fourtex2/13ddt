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
            relheight=.1,
            anchor='center'
            )
        username_label = tk.Label(
            loginframe,
            text="ENTER USERNAME"
            )
        
        username_label.place(relx=.3,rely=.3,relwidth=.4,relheight=.25, anchor='center')
        username_entry = tk.Entry(loginframe)

        username_entry.place(relx=.65,rely=.3,relwidth=.4,relheight=.25, anchor='center')
        password_label = tk.Label(loginframe, text="password")

        password_label.place(relx=.3,rely=.6,relwidth=.4,relheight=.25, anchor='center')
        password_entry = tk.Entry(loginframe)
        
        password_entry.place(relx=.65,rely=.6,relwidth=.4,relheight=.25, anchor='center')

        nextpageframe = tk.Frame(self,bg='blue')

        incorrect_login_label = tk.Label(
            root,text="INCORRECT USERNAME OR PASSWORD",bg='grey'
        )
        add_new_user_blank = tk.Label(
            root,text="Please add a username or password",bg='grey'
        )
        add_new_user_too_long = tk.Label(
            root,text="Username or password is too long",bg='grey'
        )
        add_new_user_already_taken = tk.Label(
            root,text="Username already taken",bg='grey'
        )
        add_new_user_success = tk.Label(
            root,text="Account created!",bg='grey'
        )

        add_new_user_frame = tk.Frame(self, bg="blue")

        add_new_username_label = tk.Label(add_new_user_frame, text="username")
        add_new_username_label.place(relx =.5,
                                     rely=.1,
                                     relwidth=.6,
                                     relheight=.1,
                                     anchor='center')

        add_new_username_entry = tk.Entry(add_new_user_frame)
        add_new_username_entry.place(relx =.5,
                                     rely=.3,
                                     relwidth=.6,
                                     relheight=.1,
                                     anchor='center')

        add_new_password_label = tk.Label(add_new_user_frame, text="password")
        add_new_password_label.place(relx =.5,
                                     rely=.5,
                                     relwidth=.6,
                                     relheight=.1,
                                     anchor='center')

        add_new_password_entry = tk.Entry(add_new_user_frame)
        add_new_password_entry.place(
                                        relx =.5,
                                        rely=.7,
                                        relwidth=.6,
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
                add_new_user_blank.place(relx=.5,
                                            rely=.5,
                                            relheight=.1,
                                            relwidth=.2,
                                            anchor='center')
                add_new_user_blank.after(1000,
                                         add_new_user_blank.place_forget)
                return
            
            if len(entered_new_password) >= 25 or len(entered_new_username) >= 25:
                print("Username or password too long")
                add_new_user_too_long.place(relx=.5,
                                            rely=.5,
                                            relheight=.1,
                                            relwidth=.2,
                                            anchor='center')
                add_new_user_too_long.after(1000,
                                            add_new_user_too_long.place_forget)
                return
            
            if check_username(entered_new_username):
                print("Username already exists")
                add_new_user_already_taken.place(relx=.5,
                                            rely=.5,
                                            relheight=.1,
                                            relwidth=.2,
                                            anchor='center')
                add_new_user_already_taken.after(
                    1000,
                    add_new_user_already_taken.place_forget
                )
                return
            
            if add_user(entered_new_username, entered_new_password):
                print("Account created!")
                add_new_user_success.place(relx=.5,
                                            rely=.5,
                                            relheight=.1,
                                            relwidth=.2,
                                            anchor='center')
                add_new_user_success.after(1000,
                                           add_new_user_success.place_forget)
                add_new_user_frame.place_forget()
                return

        submit_new_user_button = tk.Button(add_new_user_frame,
                                           text="Submit",
                                           command=check_user)
        submit_new_user_button.place(relx=.5,
                                    rely=.9,
                                    relheight=.1,
                                    relwidth=.2,
                                    anchor='center')

        self.add_new_user_button = tk.Button(root,
                                        text="add new user",
                                        command=lambda:add_new_user_frame.place(
                                            relx=.5,
                                            rely=.5,
                                            relheight=.4,
                                            relwidth=.3,
                                            anchor='center'
                                        )
        )
        self.add_new_user_button.place(relx=.5,rely=0.75,relwidth=.1,relheight=.1,anchor='center')

        def login():
            entered_name = username_entry.get()
            entered_password = password_entry.get()

            if check_login(entered_name, entered_password):
                self.add_new_user_button.place_forget()
                from maingame import game
                root.show_frame(game)

            else:
                print("Incorrect username or password")
                incorrect_login_label.place(relx=.5,
                                            rely=.5,
                                            relheight=.1,
                                            relwidth=.2,
                                            anchor='center')
                incorrect_login_label.after(
                    1000,
                    incorrect_login_label.place_forget
                )

        
        nextpageframe.place(relx=.5,
                            rely=0.9,
                            relwidth=.1,
                            relheight=.1,
                            anchor='center')
        nextpagebutton = tk.Button(nextpageframe, text="next page", command=login)
        nextpagebutton.place(relx=.5,
                             rely=0.5,
                             relwidth=.9,
                             relheight=.9,
                             anchor='center')


        closewindowframe = tk.Frame(self,bg='red')
        closewindowframe.place(relx=.9
                               ,rely=0.9,
                               relwidth=.07,
                               relheight=.07,
                               anchor='center')
        
        closebutton = tk.Button(closewindowframe, text="close", command=lambda:root.destroy())
        closebutton.place(relx=.5,
                          rely=0.5,
                          relwidth=.9,
                          relheight=.9,
                          anchor='center')

        # icon = ImageTk.PhotoImage(Image.open("window_icon_placeholder.png"))
        # root.iconbitmap(icon)
