from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please fill in all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# ---------------------------- Canvas ------------------------------- #
canvas = Canvas(width=200, height=200)
password_image = PhotoImage(file=r"C:\Users\tyt36\OneDrive\Desktop\All\GitDemo\passwordmanager\logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(column=1, row=0, columnspan=2, pady=(0, 20))

# ---------------------------- Website Entry ------------------------------- #
website_label = Label(text="Website:", font=("times to roman", 8, "bold"))
website_label.grid(column=0, row=1, sticky="w")

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="w")  
website_label.focus()
# ---------------------------- Email/Username Entry ------------------------------- #
email_label = Label(text="Email/Username:", font=("times to roman", 8, "bold"))
email_label.grid(column=0, row=2, sticky="w")

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2, sticky="w")
email_input.insert(0, "paramesh@gmail.com")

# ---------------------------- Password Entry ------------------------------- #
password_label = Label(text="Password:", font=("times to roman", 8, "bold"))
password_label.grid(column=0, row=3, sticky="w")

password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="w")

generate_password_button = Button(text="Generate Password", font=("times to roman", 8, "bold"), command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="w")  

# ---------------------------- Add Button ------------------------------- #
add_button = Button(text="Add", font=("times to roman", 8, "bold"), width=36, command= save)
add_button.grid(column=1, row=4, columnspan=2, pady=(10, 0))

window.mainloop()
