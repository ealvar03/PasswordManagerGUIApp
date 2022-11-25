from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_of_lists = []
    letter_list = [choice(letters) for char in range(randint(8, 10))]
    symbols_list = [choice(symbols) for character in range(randint(2, 4))]
    numbers_list = [choice(numbers) for number in range(randint(2, 4))]

    list_of_lists.append(letter_list)
    list_of_lists.append(symbols_list)
    list_of_lists.append(numbers_list)
    password_list = [char for sublist in list_of_lists for char in sublist]
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(url_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=url_entry.get(),
                                       message=f"Details entered: \nEmail: {mail_entry.get()} \nPassword: "
                                               f"{password_entry.get()} \nIs it correct?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(url_entry.get() + " | " + mail_entry.get() + " | " + password_entry.get() + "\n")
            file.close()

            url_entry.delete(0, END)
            mail_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=180, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website")
website.grid(column=0, row=1)
user_mail = Label(text="Email/Username")
user_mail.grid(column=0, row=2)
password = Label(text="Password")
password.grid(column=0, row=3)

# Entries
url_entry = Entry(width=35)
url_entry.grid(column=1, row=1, columnspan=2)
url_entry.focus()
mail_entry = Entry(width=35)
mail_entry.grid(column=1, row=2, columnspan=2)
mail_entry.insert(0, "example@email.com")
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password", width=11, command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(width=33, text="Add", command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
