import tkinter as tk
from tkinter import *
from reserva import Reserva


class VerificacaoDeEntrada:
    def __init__(self, rio, curitiba, saopaulo , airbus, boeing, embraer):
        rio = rio.get()
        curitiba = curitiba.get()
        saopaulo = saopaulo.get()
        airbus = airbus.get()
        boeing = boeing.get()
        embraer = embraer.get()
        while rio == 0 and curitiba == 0 and saopaulo == 0:
            print('impossivel cadastrar')
            return
        while rio == 1 and curitiba == 1 and saopaulo == 1:
            print('impossivel cadastrar')
            return
        while rio == 1 and saopaulo == 1:
            print('impossivel cadastrar')
            return
        while rio == 1 and curitiba == 1:
            print('impossivel cadastrar')
            return
        while saopaulo == 1 and curitiba == 1:
            print('impossivel cadastrar')
            return
        while airbus == 0 and boeing == 0 and embraer == 0:
            print('impossivel cadastrar')
            return
        while airbus == 1 and boeing == 1 and embraer == 1:
            print('impossivel cadastrar')
            return
        while airbus == 1 and boeing == 1:
            print('impossivel cadastrar')
            return
        while airbus == 1 and embraer == 1:
            print('impossivel cadastrar')
            return
        while boeing == 1 and embraer == 1:
            print('impossivel cadastrar')
            return
        else:
            Reserva()



class app:
    def __init__(self):
        main = tk.Tk()
        ## dimensões da pagina
        self.main = main.geometry("400x350")
        self.title = main.title("Titulo")
        ## minimos pixel possiveis
        self.minResolusao = main.minsize(400, 350)
        self.maxResolusao = main.maxsize(400, 350)
        ## cor de fundo
        main.configure(background='#3B87EB')


        #####################################################################################################
        ## PARTE DO CÓDIGO DO MENU DE DESTINOS
        fr_div = Frame(main, borderwidth=3, relief="solid")
        fr_div.place(x=10,y=10,width=380,height=45)
        self.rioJ = IntVar()
        self.checked_rio = Checkbutton(main, text='Rio de Janeiro', variable=self.rioJ , onvalue=1, offvalue=0)
        self.checked_rio.place(x = 30, y = 20)
        self.curitiba = IntVar()
        self.checked_curitiba = Checkbutton(main, text='Curitiba', variable=self.curitiba, onvalue=1, offvalue=0)
        self.checked_curitiba.place(x = 170, y = 20)
        self.saoP = IntVar()
        self.checked_saoP = Checkbutton(main, text='São Paulo', variable=self.saoP, onvalue=1, offvalue=0)
        self.checked_saoP.place(x = 280, y = 20)
        #####################################################################################################

        ## PARTE DO CÓDIGO DE MENU DE AERONAVES
        fr_div2 = Frame(main, borderwidth=3, relief='solid')
        fr_div2.place(x=10,y=60,width=380,height=45)
        self.embraer = IntVar()
        checked_Embraer = Checkbutton(main, text='Embraer 195', variable=self.embraer, onvalue=1 , offvalue=0)
        checked_Embraer.place(x = 30, y = 70)
        self.boeing = IntVar()
        checked_Boeing = Checkbutton(main, text='Boeing 737', variable=self.boeing, onvalue=1 , offvalue=0)
        checked_Boeing.place(x = 170, y = 70)
        self.airbus = IntVar()
        checked_Airbus = Checkbutton(main, text='Airbus A319', variable=self.airbus, onvalue=1 , offvalue=0)
        checked_Airbus.place(x = 280, y = 70)

        #####################################################################################################
        
        fr_main = Frame(main, borderwidth=1, relief='solid')
        fr_main.place(x=10,y=110,height=110,width=380)
        #####################################################################################################
        ## OPÇÃO 2
        ## Label opção 2
        lblOpcao_twoo = tk.Label(main, text ="Realizar reserva ->")
        lblOpcao_twoo.place(x = 50, y = 115)
        ## Botão opção 2 
        reserva = tk.Button(main, text="Realizar", bg='white', background='#163359', foreground='white', command=lambda:VerificacaoDeEntrada(self.rioJ, self.curitiba, self.saoP, self.airbus, self.boeing, self.embraer))
        reserva.place(x = 210, y = 115, width = 155)
        ######################################################################################################
        ## opção 3
        ## Label opção 3
        lblOpcao_tree = tk.Label(main, text ="Visualizar poltronas ->" )
        lblOpcao_tree.place(x = 40, y = 150)
        ## Botão opção 3
        visualizar_poltro = tk.Button(main, text="Visualizar", bg='white' , background='#163359', foreground='white')
        visualizar_poltro.place(x = 210, y = 150, width = 155)
        #####################################################################################################
        ## opção 4
        ## Label opção 4
        lblOpcao_for = tk.Label(main, text ="Consultar lista de passageiros ->" )
        lblOpcao_for.place(x = 20, y = 190)
        ## Botão opção 4
        consulta_Passa = tk.Button(main, text="Consultar", bg='white' , background='#163359', foreground='white')
        consulta_Passa.place(x = 210, y = 187, width = 155)

        
        
        
        
        #####################################################################################################
        ## opção sAIR
        ## Label opção 5
        lblOpcao_five = tk.Label(main, text ="Sair do sistema ->", background='#3B87EB' )
        lblOpcao_five.place(x = 200, y = 315)
        ## Botão opção 5
        sairsistema = tk.Button(main, text="Sair", bg='white', foreground='white', background='Red', command = main.destroy)
        sairsistema.place(x = 300, y = 310, width = 85, height=30)
        ######################################################################################################
        main.mainloop()


app()
