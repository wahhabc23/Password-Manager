# ---------------------------- IMPORTS ------------------------------- #
import tkinter
from tkinter import messagebox
from random import shuffle, choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    password_entry.delete(0, tkinter.END)

    password_list = [choice(letters) for _ in range(6)] + [choice(numbers)
                                                           for _ in range(3)] + [choice(symbols) for _ in range(3)]
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    user = user_entry.get()
    site = website_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You left some fields empty")
    else:
        is_ok = messagebox.askokcancel(
            title=site, message=f"These are the values entered :\n\tEmail: {user}\n\tWebsite: {site}\n\tPassword: {password}.\n\nClick OK to Confirm")
        if is_ok:
            with open('data.txt', 'a') as data:
                data.write(f"{user} | {site} | {password}\n")
                data.close()
            password_entry.delete(0, tkinter.END)
            website_entry.delete(0, tkinter.END)
            website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
screen = tkinter.Tk()
screen.title('Password Manager')
screen.config(padx=50, pady=50,background='white')
canvas = tkinter.Canvas(width=200, height=200, highlightthickness=0, background='white')
img = tkinter.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=img)
website_label = tkinter.Label(text='Website', background='white')
website_entry = tkinter.Entry(width=35, background='#F7F7F7')
website_entry.focus()
with open('data.txt', 'r') as data:
    emails_list = data.readlines()
    if emails_list:
        default_email = emails_list[-1].split()
    else:
        default_email = ['sample@email.com']
    data.close() # Set last email to deafult
user_label = tkinter.Label(text='Username/Email',background='white')
user_entry = tkinter.Entry(width=35, background='#F7F7F7')
user_entry.insert(0, default_email[0])
password_label = tkinter.Label(text='Password', background='white')
password_entry = tkinter.Entry(width=21, background='#F7F7F7')
generate_button = tkinter.Button(
    text='Generate', width=11, pady=0, command=generate_password, borderwidth=2)
add_button = tkinter.Button(text='Add', width=30, command=save_password, borderwidth=2)


# ---------------------------- LAYOUT ------------------------------- #
canvas.grid(row=0, column=1)
user_label.grid(row=1, column=0)
user_entry.grid(row=1, column=1, columnspan=2)
website_label.grid(row=2, column=0)
website_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)


# ---------------------------- END ------------------------------- #
screen.mainloop()
