import tkinter as tk
from tkinter import *


class VerificacaoLog:
    def __init__(self, email, senha, janela):
        acesso = [{'email':'railan.ufsc', 'senha':'123456'},{'email':'thalles.ufsc', 'senha':'123456'}]
        email = str(email.get())
        senha = str(senha.get())
        janela = janela
    
        for i in acesso:
            if email in i.values():
                permissao = True
                break
            else:
                permissao = False
        for i in acesso:
            if senha in i.values():
                password = True
                break
            else:
                password = False

        if permissao == True and password == True:
            import menu
            # estou fazendo um comando para destruir a pagina de log assim que logar
            janela.destroy()
            menu()
        else:
            print('Acesso negado!')