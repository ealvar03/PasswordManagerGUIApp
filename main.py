from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_of_lists = []
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

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
    website = url_entry.get()
    mail = mail_entry.get()
    password_inf = password_entry.get()
    new_data = {website: {
        "email": mail,
        "password": password_inf
    }
    }
    if len(website) == 0 or len(password_inf) == 0:
        messagebox.showinfo(title="Oops", message="Please, don't leave any fields empty")
    else:
        try:
            file = open("data.json", "r")
            # Reading stored data
            data = json.load(file)
        except FileNotFoundError:
            # If file does not exist, create a new one
            file = open("data.json", "w")
            json.dump(new_data, file, indent=4)
        else:
            # Updte old data with the new data
            data.update(new_data)
            file.close()
            file = open("data.json", "w")
            # Save updated data in the existing file
            json.dump(data, file, indent=4)
            file.close()
        finally:
            url_entry.delete(0, END)
            password_entry.delete(0, END)


# ----------------------- FIND PASSWORD --------------------- #

def find_password():
    url = url_entry.get()
    try:
        with open("data.json", "r") as file:
            json_content = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        for item in json_content:
            if url.lower() in item.lower():
                messagebox.showinfo(title=url, message=f"Email: {json_content[item]['email']}\nPassword: "
                                                       f"{json_content[item]['password']}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {url} exists.")


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
url_entry = Entry(width=20)
url_entry.grid(column=1, row=1)
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
search_button = Button(text="Search", width=11, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
