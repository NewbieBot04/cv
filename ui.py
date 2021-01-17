from tkinter import *
from PIL import ImageTk, Image


class UserInterface:
    def __init__(self):
        self.names = []
        self.emails = []
        self.window = Tk()
        self.window.title(string="FLIGHT CLUB")
        self.window.config(padx=50, pady=50, bg="light blue")
        self.img = ImageTk.PhotoImage(Image.open("try.jpg"))
        self.canvas = Canvas(width=500, height=300, highlightthickness=0, bg="light blue")
        self.canvas.create_image(250, 100, image=self.img)
        self.canvas.grid(row=0, column=0, columnspan=7)

        self.name_label = Label(text="Name: ", fg="black", bg="grey", font=("arial", 10, "normal"))
        self.name_label.grid(row=2, column=1, pady=5)
        self.name_entry = Entry(width=30)
        self.name_entry.focus()
        self.name_entry.grid(row=2, column=2)

        self.email_label = Label(text="Email: ", fg="black", bg="grey", font=("arial", 10, "normal"))
        self.email_label.grid(row=3, column=1, pady=5)
        self.email_entry = Entry(width=60)
        self.email_entry.grid(row=3, column=2, columnspan=2)
        self.enter_button = Button(text="CLICK TO REGISTER", width=15, bg="grey", command=self.getting_details)
        self.enter_button.grid(row=5, column=2, pady=10)
        self.window.mainloop()

    def getting_details(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        self.names.append(name)
        self.emails.append(email)







