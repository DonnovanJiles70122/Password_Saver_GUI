from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

######################
# PASSWORD GENERATOR #
######################

def generate_password():
#Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

#################
# SAVE PASSWORD #
#################

def save_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(password) == 0 or  len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # reading old data
                load_data = json.load(data_file)
        # If json file doesn't exist create it and write data to file
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # Updating old data with new data
            load_data.update(data)

            # If file exist open file and write data to it
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(load_data, data_file, indent=4)
        finally:
            # Delete entries
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)

#################
# FIND PASSWORD #
#################

def search_data():
    website = website_input.get()

    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave website field empty.")
    else:
        try:
            with open('data.json', 'r') as data_file:
                # reading old data
                load_data = json.load(data_file)
        # If json file doesn't exist send error message
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="You haven't saved any passwords")
        else:
            if website in load_data:
                username = load_data[website]["username"]
                password = load_data[website]["password"]

                messagebox.showinfo(title=website, message=f"Username : {username} \n Password : {password}")
            else:
                messagebox.showinfo(title="Website not found", message=f"the website {website}'s username and password "
                                    "has not been saved yet")
        finally:
            website_input.delete(0, END)

    



############
# UI SETUP #
############

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="White")

canvas = Canvas(width=200, height=200, bg="White", highlightthickness=0)
lock_image = PhotoImage(file="lock-icon.png")
canvas.create_image(100, 90, image=lock_image)
canvas.grid(column=1, row=0)

# Labels
# Create Labels
website_label = Label(text="Website", bg="White")
username_label = Label(text="E-mail/Username:", bg="White")
password_label = Label(text="Password", bg="White")

# Place Labels
website_label.grid(column=0, row=1, pady=10)
username_label.grid(column=0, row=2, pady=10)
password_label.grid(column=0, row=3, pady=10)

# Entry
# Create Entry
website_input = Entry(width=22, highlightthickness=2, highlightbackground="grey")
username_input = Entry(width=40, highlightthickness=2, highlightbackground="grey")
password_input = Entry(width=22, highlightthickness=2, highlightbackground="grey")


# Place Entry
website_input.grid(column=1, row=1, pady=10)
website_input.focus()
username_input.grid(column=1, columnspan=2, row=2, pady=10)
username_input.insert(0, "djiles@mail.sfsu.edu")
password_input.grid(column=1, row=3, pady=10)

# Button
# Create Button
search_button = Button(text="Search", width=15 , command=search_data)
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_password)


# Place Button
search_button.grid(column=2, row=1, pady=10)
generate_button.grid(column=2, row=3, pady=10)
add_button.grid(column=1, columnspan=2, row=4, pady=10)



window.mainloop()