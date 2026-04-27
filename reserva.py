import tkinter

import sqlite3
import random

anuncio = open("Banco-Investimento--Trabalho-Rad/anuncios.txt","r").read()

ad1,ad2,ad3 = anuncio.split("\n")

usuario = ""
Renda = 0

conectar = sqlite3.connect('Banco-Investimento--Trabalho-Rad/bancoRenda.db')
cursor = conectar.cursor()


def Pesquisar():
        global usuario
        global Renda
        usuario = (usuario_input.get())
        resultado.config(text=usuario,fg="#1F222E")

        renda_pura = cursor.execute(f"SELECT Renda FROM Banco WHERE Usuario = '{usuario}'").fetchall()

        Renda = int(renda_pura[0][0])

        print(Renda)
        if  (Renda >= 15000):
                resultado.config(text="Acesso Liberado",fg="#1FBF65")
                telaDosRicos(appbanco)
        elif (Renda < 15000):
                resultado.config(text="Acesso Negado",fg="#FA114F")
                telaDosPobres(appbanco)


def roletarussa(a):
        lista = ["1", "2", "3","4","5","6","7","8","9","10"]

        r =random.choice(lista)
        if r == '1':
            a.config(text="não ganho nada 0%",fg="#000000")
        elif r == '2':
            a.config(text="voce esta pobre -11111100%",fg="#CE0F2F")
        elif r == '3':
            a.config(text="um milhao de dolares de lucro 777777%",fg="#17912C")
        elif r == '4':
            a.config(text="voce ganhou uma capiavara \nmas perdeu tudo, de lucro -456356535465%",fg="#DB460B")
        elif r == '5':
            a.config(text="não ganho nada 0%",fg="#000000")
        elif r == '6':
            a.config(text="Voce é dono do mundo de \nlucros 11230123213120%",fg="#17912C")
        elif r == '7':
                a.config(text="Voce achou um peixe podre mais ganhou \nem dobro de lucros 3232423%",fg="#17912C")
        elif r == '8':
            a.config(text="0% lucros",fg="#000000")
        elif r == '9':
            a.config(text=" 10% de lucros",fg="#A6B427")
        elif r == '10':
            a.config(text=" 67% de lucros hehe",fg="#2FB946")

def telaDosRicos(appbanco):

        investir = tkinter.Toplevel(appbanco)
        investir.resizable(False, False)
        investir.title("Investimentos")
        investir.geometry("400x500")
        
        nome = tkinter.Label(investir, text = f"Bem-Vindo {usuario}\nSeu saldo: \n{Renda}",font=("Comic Sans Ms", 16))
        nome.pack()

        texto2 = tkinter.Label(investir, text = "Anuncios",font=(18))
        texto2.pack() 

        close = tkinter.Button(investir, text="Fechar", command=investir.destroy)
        close.pack

        #1
        popup1 = tkinter.Label(investir, text = ad1)
        popup1.pack()

        lucro1 = tkinter.Label(investir, text = "valor do mercado: \n11000",font=("Comic Sans Ms", 12))
        lucro1.pack()

        bt1 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro1),activebackground="#F21111",font=(15))
 
        bt1.pack(pady=5)

        #2
        popup2 = tkinter.Label(investir, text = ad2)
        popup2.pack()

        lucro2 = tkinter.Label(investir, text = "valor do mercado: \n900",font=("Comic Sans Ms", 12))
        lucro2.pack()

        bt2 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro2),activebackground="#F21111",font=(15))
 
        bt2.pack(pady=5)
        popup3 = tkinter.Label(investir, text = ad3)
        popup3.pack()

        lucro3 = tkinter.Label(investir, text = "valor do mercado: \n10000",font=("Comic Sans Ms", 12))
        lucro3.pack()
        bt3 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro3),activebackground="#F21111",font=(15))
        
        bt3.pack(pady=5)

def telaDosPobres(appbanco):

        anuncios = tkinter.Toplevel(appbanco)
        anuncios.resizable(False, False)
        anuncios.title("Anuncios")
        anuncios.geometry("400x500")
        
        nome = tkinter.Label(anuncios, text = "Bem-Vindo " + usuario,font=("Comic Sans Ms", 16))
        nome.pack()

        txt1 = tkinter.Label(anuncios, text = "Você não possui o necessario para investir mas sinta-se",font=(20), fg="#CE0F2F")
        txt1.pack() 

        ad1 = tkinter.Label(anuncios, text = "Invista na estacao de ca\n Vem pra ca do outro lado ",font=(20))
        ad1.pack() 

        ad2 = tkinter.Label(anuncios, text = "Invista na mc ronalds\n invista aqui nos temos um palhaço de 50 anos com cara de 10",font=(20))
        ad2.pack() 

        ad3 = tkinter.Label(anuncios, text = "Invista na border king\nÉ o restaurante que te faz atravessar fronteiras",font=(20))
        ad3.pack() 
        

        close = tkinter.Button(anuncios, text="Fechar", command=anuncios.destroy)
        close.pack

#padrao
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

txt1 = tkinter.Label(appbanco, text = "Usuario")
txt1.pack()
entrada1 = tkinter.Entry(appbanco, textvariable=usuario_input,width=10,font=("Arial", 18))
entrada1.pack(pady=10)

resultado = tkinter.Label(appbanco, text = "",font=("Comic Sans Ms", 16))
resultado.pack()

btn = tkinter.Button(appbanco, text="Entrar",command=Pesquisar,activebackground="#3A556E",width=5, height=2,font=(15))
btn.pack(pady=5)

appbanco.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs


conectar.commit()

conectar.close()