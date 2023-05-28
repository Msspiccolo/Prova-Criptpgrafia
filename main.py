from tkinter import *
from tkinter.ttk import *
import string


def encript(texto):
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    key.reverse()

    key = list(key)

    texto_encriptografado = ""

    for letra in texto:
        index = chars.index(letra)
        texto_encriptografado += key[index]

    return texto_encriptografado





def encriptSingleWay(password_entry):
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
        file.write(loginSignup.get() + " " + encriptSingleWay(passwordSignup.get()) + "\n")
        file.close()
        newWindow.destroy()

    btn = Button(newWindow, text="Clique aqui para fazer signUp", command=signup)
    btn.pack(pady=10)


def encriptografar():
    novaJanela = Toplevel(master)
    novaJanela.title("Encriptografar")
    novaJanela.geometry("200x200")

    Label(novaJanela, text="Texto para encriptografar").pack()
    texto = Entry(novaJanela, width=30)
    texto.pack()

    def encript():
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy()
        key.reverse()

        key = list(key)

        texto_encriptografado = ""

        for letra in texto.get():
            index = chars.index(letra)
            texto_encriptografado += key[index]

        file = open("encriptografado.txt", "a")
        file.write(texto_encriptografado + "\n")
        file.close()

    btn = Button(novaJanela, text="Clique aqui para encriptografar", command=encript)

    btn.pack(pady=10)

    texto_descriptografado_label = Label(novaJanela, text="Texto descriptografado: ")
    texto_descriptografado_label.pack()

    def decript():
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        key = chars.copy()
        key.reverse()
        key = list(key)
        file = open("encriptografado.txt", "r")
        texto_encriptografado = file.readlines()[0]
        file.close()
        texto_descriptografado = ""

        for letter in list(texto_encriptografado):
            index = key.index(letter)
            texto_descriptografado += chars[index]

        texto_descriptografado_label["text"] = "Texto descriptografado: " + texto_descriptografado


    btnDesc = Button(novaJanela, text="Clique aqui para descriptografar", command=decript)
    btnDesc.pack(pady=10)

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
        if user[0] == userlogin and user[1] == encriptSingleWay(userpassword):
            encriptografar()
            break
    else:
        print("Login ou senha incorretos")


btn = Button(master, text="Clique aqui para fazer login", command=logIn)
btn.pack(pady=10)

mainloop()
