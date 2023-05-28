from tkinter import *
from tkinter.ttk import *
import string


def encript(password_entry):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = "qwertyuiopasdfghjklzxcvbnm"

    key = key * len(chars)

    key = list(key)

    senha = password_entry
    cipher_text = ""

    for letra in senha:
        index = chars.index(letra)
        cipher_text += key[index]

    return cipher_text


def openNewWindow():
    newWindow = Toplevel(master)

    newWindow.title("Signup")

    newWindow.geometry("200x200")

    Label(newWindow, text="Login").pack()
    loginSignup = Entry(newWindow, width=30)
    loginSignup.pack()

    Label(newWindow, text="Password").pack()
    passwordSignup = Entry(newWindow, width=30)
    passwordSignup.pack()

    def signup():
        file = open("users.txt", "a")
        file.write(loginSignup.get() + " " + encript(passwordSignup.get()) + "\n")
        file.close()
        newWindow.destroy()

    btn = Button(newWindow, text="Clique aqui para fazer signUp", command=signup)
    btn.pack(pady=10)


master = Tk()

master.geometry("200x200")
master.title("Login")

Label(master, text="Login").pack()
login = Entry(master, width=30)
login.pack()

Label(master, text="Password").pack()
password = Entry(master, width=30)
password.pack()

btn = Button(master, text="Clique aqui para fazer signUp", command=openNewWindow)
btn.pack(pady=10)


def logIn():
    userlogin = login.get()
    userpassword = password.get()

    file = open("users.txt", "r")
    users = file.readlines()
    file.close()

    for user in users:
        user = user.split()
        if user[0] == userlogin and user[1] == encript(userpassword):
            print("Login realizado com sucesso")
            break
    else:
        print("Login ou senha incorretos")


btn = Button(master, text="Clique aqui para fazer login", command=logIn)
btn.pack(pady=10)

mainloop()