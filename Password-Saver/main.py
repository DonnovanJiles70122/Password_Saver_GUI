from tkinter import *
from tkinter import messagebox
import random
import pyperclip

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
    data = []
    data.append(website_input.get())
    data.append(username_input.get())
    data.append(password_input.get())

    if len(data[0]) == 0 or len(data[1]) == 0 or len(data[2]) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=data[0], message=f"These are the details entered: \nEmail : {data[1]} "
                            f"\nPassword: {data[2]} \nIs it ok to save")
        
        if is_ok:
            website_input.delete(0, END)
            username_input.delete(0, END)
            password_input.delete(0, END)
            
            print("data = " , data)

            with open('data.txt', 'a') as file:
                file.write("\n")
                for element in data:
                    file.write(element)
                    file.write(" | ")
                file.write("\n-------------------------")




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
website_label.grid(column=0, row=1)
username_label.grid(column=0, row=2)
password_label.grid(column=0, row=3)

# Entry
# Create Entry
website_input = Entry(width=40)
username_input = Entry(width=40)
password_input = Entry(width=22)


# Place Entry
website_input.grid(column=1, columnspan=2, row=1)
website_input.focus()
username_input.grid(column=1, columnspan=2, row=2)
username_input.insert(0, "djiles@mail.sfsu.edu")
password_input.grid(column=1, row=3)

# Button
# Create Button
generate_button = Button(text="Generate Password", command=generate_password)
add_button = Button(text="Add", width=36, command=save_password)

# Place Button
generate_button.grid(column=2, row=3)
add_button.grid(column=1, columnspan=2, row=4)



window.mainloop()