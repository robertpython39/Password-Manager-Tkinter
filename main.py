#-------------------------------------------------------------------------------
# Name:        Password Manager
# Purpose:     Fun
#
# Author:      nicolescu
#
# Created:     29/03/2022
# Copyright:   (c) nicol 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------


from tkinter import *
from tkinter import messagebox
import random
import os

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = list("ABCDEFGHIJKLMNOPQRSTUVVWXYZabcdefghijklmnopqrstuvwxyz")
    numbers = list("123456789")
    symbols = list("!@#$%^&*()")

    nr_letters = [random.choice(letters) for letter in range(random.randint(8, 10))]
    nr_numbers = [random.choice(numbers) for number in range(random.randint(3, 5))]
    nr_symbols = [random.choice(symbols) for symbol in range(random.randint(3, 5))]

    temp_pass = nr_letters + nr_symbols + nr_numbers
    random.shuffle(temp_pass)
    password = "".join(temp_pass)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get().title()
    username = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        message = messagebox.showinfo(title="Error", message="Please fill field/fields! ")
    else:
        message = messagebox.askokcancel(title="Verify", message=f"Username: {username}\n"
                                                          f"Password: {password}\n Are they correct?")
        if message == True:
            with open("passwords.txt", "a") as data:
                data.write(f"Website: {website.title()} | User: {username} | Password: {password}\n")
                data.close()
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = website_entry.get().title()
    try:
        with open("passwords.txt") as data_file:
            if website in data_file:
                messagebox.showinfo(title="Password and Username",
                                    message=f"Data about the website:{data_file.readlines()[website]}")
            else:
                messagebox.showinfo(title="Error",
                                    message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found!")

    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(height=201, width=201)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
created_by = Label(text="Created by Robert Mihai NICOLESCU", font=("Tahoma", 7, "italic"), fg="red")
created_by.grid(column=3, row=5)
#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "robert.nicolescu1992@gmail.com")
password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

# Buttons
generate_password_button = Button(text="Generate\nPassword", command=password_generate)
generate_password_button.grid(row=3, column=2, columnspan=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)
search = Button(text="Search", command=search_website)
search.grid(column=2, row=1, columnspan=1)

window.mainloop()
