from tkinter import *
from tkinter import messagebox
import random
import json
#---------------------------- PASSWORD GENERATOR -------------------------------#

def Search_web():
    web = website_input.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
            if web in data:
                email = data[web]["email/username"]
                password=data[web]["password"]
                messagebox.showinfo(title=web, message=f"Email:{email}\nPassword:{password}")

            else:
                messagebox.showinfo(title="website status", message="the Website not found")
    except FileNotFoundError:
        messagebox.showinfo(title="File status", message="the File not found")



def make_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
      password_list.append(random.choice(letters))

    for char in range(nr_symbols):
      password_list += random.choice(symbols)

    for char in range(nr_numbers):
      password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char
    password_input.delete(0,'end')
    password_input.insert( 0, password)
    return 1
#---------------------------- SAVE PASSWORD -------------------------------#
def Save():
    web = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data ={
        web: {
            "email/username": email,
            "password": password,
        }
    }

    if (not web or  not email or not password):
        messagebox.askokcancel(title="error", message="Don't leave a blank space.")

    else:
        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)


        except FileNotFoundError:
            with open("passwords.json","w") as f:
                json.dump(new_data, f, indent=4)

        else:
            data.update(new_data)
            with open("passwords.json","w") as f:
                json.dump(data, f, indent=4)


        finally:
            website_input.delete(0, 'end')
            email_input.delete(0, 'end')
            password_input.delete(0, 'end')

#---------------------------- UI  -------------------------------#
window = Tk()
window.title("Python Password Manager")
window.config(pady=50, padx=50, bg="BLACK")
window.resizable(False, False)

# Canvas
new_canvas = Canvas(width=200, height=200, bg="BLACK", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
new_canvas.create_image(100, 100, image=logo_img)
new_canvas.grid(row=0, column=1, columnspan=2)

# Labels
website_label = Label(text="Website: ", bg="BLACK", fg="GRAY", font="Arial 12")
email_label = Label(text="Email/Username: ", bg="BLACK", fg="GRAY", font="Arial 12")
password_label = Label(text="Password: ", bg="BLACK", fg="GRAY", font="Arial 12")
website_label.grid(row=1, column=0, pady=(0, 10))
email_label.grid(row=2, column=0, pady=(0, 10))
password_label.grid(row=3, column=0, pady=(0, 10))
'''search_label = Label(text="Website: ", bg="BLACK", fg="GRAY", font="Arial 12")
search_label = Label(text="Search: ", bg="BLACK", fg="GRAY", font="Arial 12")'''

# Input
website_input = Entry(font="Arial 12")
website_input.grid(row=1, column=1, sticky="WE", ipady=5, pady=(0, 10),padx=(0, 10))
website_input.focus()
email_input = Entry(font="Arial 12")
email_input.grid(row=2, column=1, columnspan=2, sticky="EW", ipady=5, pady=(0, 10))
password_input = Entry(font="Arial 12")
password_input.grid(row=3, column=1, sticky="EW", pady=(0, 10), ipady=5, padx=(0, 10))


# Buttons
gen_pwd_btn = Button(text="Generate password", font="Arial 10", command=make_password)
search_btn = Button(text="Search", font="Arial 10", command=Search_web)
search_btn.grid(row=1, column=2, sticky="we", pady=(0, 10), ipady=2)
gen_pwd_btn.grid(row=3, column=2, sticky="we", pady=(0, 10), ipady=2)
add_button = Button(text="Add", font="Arial 10", width=60, command=Save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", ipady=2)

window.mainloop()


