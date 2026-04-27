#interface
import tkinter

import sqlite3
import random




anuncio = open("Banco-Investimento--Trabalho-Rad/anuncios.txt","r").read()
ad1,ad2,ad3 = anuncio.split("\n")

usuario = ""


conectar = sqlite3.connect('banco.db')
cursor = conectar.cursor()
 

def Pesquisar():
        global usuario
        usuario = (usuario_input.get())
        resultado.config(text=usuario,fg="#1F222E")
        Renda = int(renda_input.get())
        rows = cursor.execute(f"SELECT renda FROM Tabela1 WHERE usuario = {usuario}").fetchall()
        
        if  (Renda >= 15000):
                resultado.config(text="Acesso Liberado",fg="#11FA76")
                anuncio(appbanco)
        elif (Renda < 15000):
                resultado.config(text="Renda menor que 15000",fg="#FA114F")
        print(rows)


def Logar():
        global usuario
        usuario = (usuario_input.get())
        resultado.config(text=usuario,fg="#1F222E")

        Renda = float(renda_input.get())
        if  (Renda >= 15000):
                resultado.config(text="Acesso Liberado",fg="#1FBF65")
                lista_investimentos(appbanco)
        elif (Renda < 15000):
                resultado.config(text="Acesso Negado",fg="#FA114F")
                lista_anuncios(appbanco)


def lista_anuncios(appbanco):
        anuncios = tkinter.Toplevel(appbanco)
        anuncios.resizable(False, False)
        anuncios.title("Anuncios")
        anuncios.geometry("300x300")
        
        nome = tkinter.Label(anuncios, text = "Bem-Vindo " + usuario,font=("Comic Sans Ms", 16))
        nome.pack()

        texto1 = tkinter.Label(anuncios, text = "Você não possui o necessario para investir",font=(20), fg="#CE0F2F")
        texto1.pack() 

        ad1 = tkinter.Label(anuncios, text = "Invista na estaco de ca",font=(20))
        ad1.pack() 

        ad2 = tkinter.Label(anuncios, text = "Invista na mc ronalds",font=(20))
        ad2.pack() 

        ad3 = tkinter.Label(anuncios, text = "Invista na border king",font=(20))
        ad3.pack() 
        

        close = tkinter.Button(anuncios, text="Fechar", command=anuncios.destroy)
        close.pack

def resultado_investimento(a):
        lista = ["1", "2", "3","4","5","6"]
        r =random.choice(lista)
        if r == '1':
            a.config(text="não ganho nada",fg="#000000")
        elif r == '2':
            a.config(text="voce esta pobre",fg="#CE0F2F")
        elif r == '3':
            a.config(text="um milhao de dolares de lucro",fg="#17912C")
        elif r == '4':
            a.config(text="voce ganhou uma capiavara mas perdeu tudo",fg="#DB460B")
        elif r == '5':
            a.config(text="não ganho nada",fg="#000000")
        elif r == '6':
            a.config(text="Voce é dono do mundo",fg="#17912C")
   
def lista_investimentos(appbanco):
        investir = tkinter.Toplevel(appbanco)
        investir.resizable(False, False)
        investir.title("Investimentos")
        investir.geometry("400x500")
        
        nome = tkinter.Label(investir, text = "Bem-Vindo " + usuario,font=("Comic Sans Ms", 16))
        nome.pack()

        texto2 = tkinter.Label(investir, text = "Anuncios",font=(18))
        texto2.pack() 

        close = tkinter.Button(investir, text="Fechar", command=investir.destroy)
        close.pack

        #1
        popup1 = tkinter.Label(investir, text = ad1)
        popup1.pack()

        lucro1 = tkinter.Label(investir, text = "11000",font=("Comic Sans Ms", 12))
        lucro1.pack()

        bt1 = tkinter.Button(investir, text="Inenstir",command=lambda: resultado_investimento(lucro1),activebackground="#F21111",font=(15))
        bt1.pack(pady=5)

        #2
        popup2 = tkinter.Label(investir, text = ad2)
        popup2.pack()

        lucro2 = tkinter.Label(investir, text = "900",font=("Comic Sans Ms", 12))
        lucro2.pack()

        bt2 = tkinter.Button(investir, text="Invenstir",command=lambda: resultado_investimento(lucro2),activebackground="#F21111",font=(15))
        bt2.pack(pady=5)

        #3
        popup3 = tkinter.Label(investir, text = ad3)
        popup3.pack()

        lucro3 = tkinter.Label(investir, text = "10000",font=("Comic Sans Ms", 12))
        lucro3.pack()
        bt3 = tkinter.Button(investir, text="Invenstir",command=lambda: resultado_investimento(lucro3),activebackground="#F21111",font=(15))
        bt3.pack(pady=5)



##interaface???
appbanco = tkinter.Tk()
appbanco.title("Banco genial")
appbanco.resizable(False, False)
appbanco.geometry("400x500")
appbanco.iconify() 
appbanco.update()
appbanco.deiconify() 
 
#p#egar o numero se nao fica igual
usuario_input = tkinter.StringVar()
renda_input = tkinter.StringVar()

texto1 = tkinter.Label(appbanco, text = "Usuario")
texto1.pack()
entrada1 = tkinter.Entry(appbanco, textvariable=usuario_input,width=10,font=("Arial", 18))
entrada1.pack(pady=40)

texto2 = tkinter.Label(appbanco, text = "Renda")
texto2.pack()
entrada2 = tkinter.Entry(appbanco, textvariable=renda_input,width=10,font=("Arial", 18))
entrada2.pack()
 
resultado = tkinter.Label(appbanco, text = "",font=("Comic Sans Ms", 16))
resultado.pack()

btn = tkinter.Button(appbanco, text="Entrar",command=Logar,activebackground="#3A556E",width=5, height=2,font=(15))
btn.pack(pady=5)

appbanco.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs

conectar.close()