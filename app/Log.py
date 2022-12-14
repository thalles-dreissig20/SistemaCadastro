import tkinter as tk
from tkinter import *
from verificalog import VerificacaoLog


class Login:
    def __init__(self):    
        self.janela = tk.Tk()
        self.janela.title('Login')
        self.janela.geometry("400x350")
        self.minResolusao = self.janela.minsize(400, 350)
        self.maxResolusao = self.janela.maxsize(400, 350)
        self.janela.configure(background='#3B87EB')

       

        lbl_email = tk.Label(self.janela, text="Email:",font=("Calibri", 15), background='#3B87EB')
        lbl_email.place(x = 20, y = 50)
        self.en_email = Entry(self.janela, bd=2, font=("Calibri", 15), justify=LEFT)
        self.en_email.place(width=362, height=40, x=20, y=80)


        lbl_senha = tk.Label(self.janela, text="Senha:",font=("Calibri", 15), background='#3B87EB')
        lbl_senha.place(x = 20, y = 120)
        self.en_senha = Entry(self.janela, bd=2, font=("Calibri", 15), justify=LEFT, show="*")
        self.en_senha.place(width=362, height=40, x=20, y=150)

        botaoLog = Button(self.janela, text="Login", foreground='white', background='blue', command=lambda:VerificacaoLog(self.en_email, self.en_senha, self.janela))
        botaoLog.place(width=113, height=40, x=250, y=200)
 
        
        img = PhotoImage(file ="./app/img/logo.png")
        label_image = Label(self.janela, image=img)
        label_image.place(x=10,y=190, height=160, width=160)

        self.janela.mainloop()

Login()