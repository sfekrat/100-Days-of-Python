from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# password generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pass():
    if len(password_entry.get()) == 0:
        password_entry.delete(0, END)
        letters_list = [choice(letters) for _ in range(randint(8, 10))]
        numbers_list = [choice(numbers) for _ in range(randint(2, 4))]
        symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
        password_list = letters_list + numbers_list + symbols_list
        shuffle(password_list)
        password = "".join(password_list)
        password_entry.insert(0, password)
        pyperclip.copy(password)


def add_password():
    website = website_text.get().lower()
    password = password_entry.get()
    email = email_user_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning('Oops', 'Some of the fields were left empty!')
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\n"
                                               f"Password: {password}")
        new_data = {
            website: {
                'email': email,
                'password': password,
            }
        }
        if is_ok:
            try:
                output = open('output.json', 'r')
                # Reading old data
                data = json.load(output)
                # Updating old data with new data
                data.update(new_data)
            except json.decoder.JSONDecodeError:
                # empty file exception
                data = new_data
            except FileNotFoundError:
                data = new_data
                output = open('output.json', 'w')
                output.close()

            with open('output.json', 'w') as output:
                # writing updated data
                json.dump(data, output, indent=4)
            messagebox.showinfo('Success', 'Password was added successfully!')
            restore()


def restore():
    website_text.delete(0, END)
    email_user_entry.delete(0, END)
    password_entry.delete(0, END)
    email_user_entry.insert(0, '@email.com')


def search():
    website = website_text.get().lower()
    try:
        with open('output.json', 'r') as output:
            data = json.load(output)
            result = f"Email: {data[website]['email']}\nPassword: {data[website]['password']}"
            messagebox.showinfo(f'{website.capitalize()}', result)
    except FileNotFoundError as error:
        messagebox.showerror('Error', f'{error}')
    except KeyError as error:
        messagebox.showerror('Error', f'Information for the {error} website was not found!')


# Window settings
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# image settings
logo = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# All labels and text areas
website_label = Label(text='Website:')
website_label.grid(column=0, row=1)
email_user_label = Label(text='Email/Username:')
email_user_label.grid(column=0, row=2)
password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Entries
website_text = Entry()
website_text.grid(column=1, row=1, columnspan=1, sticky='EW')
website_text.focus()
email_user_entry = Entry()
email_user_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
email_user_entry.insert(0, '@email.com')
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')
# generate button
generate_button = Button(text='Generate Password', command=generate_pass)
generate_button.grid(column=2, row=3)
# add button
add_button = Button(text='Add', width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')
# search button
search_button = Button(text='Search', command=search)
search_button.grid(column=2, row=1, sticky='EW')
window.mainloop()
