from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    # Made a list, thought you only could make a list with []. Peculiar, peculiar indeed
    password_list = password_letters + random_symbols + random_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data_to_file():
    # passwords = []
    # # Appending all previous data to password list
    # with open("my-pass.txt")as data:
    #     for d in data:
    #         passwords.append(d)

    # Appending new data to password list
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if password == "" and website == "":
        messagebox.showinfo(title="Fields empty", message="Both the website and password field are empty")
    elif website == "":
        messagebox.showinfo(title="Field empty", message="The username field is empty")
    elif password == "":
        messagebox.showinfo(title="Field empty", message="The password field is empty")
    else:
        is_ok = messagebox.askokcancel(title="website",
                                       message=f"These are the details entered:\nWebsite: {website} \nEmail: {username}, \nPassword: {password} \n\nIs it ok to save?")

        # passwords.append(f"{website} | {username} | {password} \n")

        # Writing to the my-pass.txt file (forgot about the append function. The former code worked, but this is a lot
        # smarter)
        if is_ok == True:
            with open("my-pass.txt", "a") as file:
                # for x in passwords:
                file.write(f"{website} | {username} | {password} \n")

            # Resetting the inputs
            website_input.delete(0, END)
            username_input.delete(0, END)
            username_input.insert(0, "nico@fake-email.com")
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("MyPass - Password Manager")
window.config(padx=20, pady=20)

# --- MyPass Image --- #
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# --- Website Input --- #
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="e")
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")

# --- Email/Username Input --- #
username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0, sticky="e")
username_input = Entry(width=35)
username_input.insert(0, "nico@fake-email.com")
username_input.grid(row=2, column=1, columnspan=2, sticky="ew")

# --- Password Input --- #
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="e")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="ew")

# --- Add Button --- #
add_button = Button(text="Add", width=44, command=save_data_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
