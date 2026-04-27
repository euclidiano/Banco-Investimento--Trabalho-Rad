import tkinter

import sqlite3
import random

anuncio = open("Banco-Investimento--Trabalho-Rad/anuncios.txt","r").read()

ad1,ad2,ad3 = anuncio.split("\n")

usuario = ""
Renda = 0

conectar = sqlite3.connect('Banco-Investimento--Trabalho-Rad/bancoRenda.db')
cursor = conectar.cursor()


def Pesquisa():
        try:
                global usuario
                global Renda
                usuario = (usuarioentrada.get())
                result.config(text=usuario,fg="#1F222E")

                renda_pura = cursor.execute(f"SELECT Renda FROM Banco WHERE Usuario = '{usuario}'").fetchall()

                Renda = int(renda_pura[0][0])

                print(Renda)
                if  (Renda >= 15000):
                        result.config(text="Investimento Liberado",fg="#1FBF65")
                        telaDosRicos(appbanco)
                elif (Renda < 15000):
                        result.config(text="Investimento Negado",fg="#FA114F")
                        telaDosPobres(appbanco)
        except:
                result.config(text="Usuário não existe",fg="#FA114F")



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
        investir.geometry("600x500")
        appbanco.iconbitmap("Banco-Investimento--Trabalho-Rad/icone.ico")
        
        nome = tkinter.Label(investir, text = f"Bem-Vindo {usuario}\nSeu saldo: \n{Renda}",font=("Arial", 16))
        nome.pack()

        espa1= tkinter.Label(investir, text = "",font=(21))
        espa1.pack(pady=5)

        texto2 = tkinter.Label(investir, text = "Anúncios",font=(21))
        texto2.pack() 

        close = tkinter.Button(investir, text="Fechar", command=investir.destroy)
        close.pack

        #1
        popup1 = tkinter.Label(investir, text = ad1,font=("Arial", 16))
        popup1.pack()

        lucro1 = tkinter.Label(investir, text = "valor do mercado: \n11000",font=("Arial", 12))
        lucro1.pack()

        bt1 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro1),activebackground="#8B1AA1",font=(15))
 
        bt1.pack(pady=5)

        #2
        popup2 = tkinter.Label(investir, text = ad2,font=("Arial", 16))
        popup2.pack()

        lucro2 = tkinter.Label(investir, text = "valor do mercado: \n900",font=("Arial", 12))
        lucro2.pack()

        bt2 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro2),activebackground="#F21111",font=(15))
 
        bt2.pack(pady=5)
        popup3 = tkinter.Label(investir, text = ad3,font=("Arial", 16))
        popup3.pack()

        lucro3 = tkinter.Label(investir, text = "valor do mercado: \n10000",font=("Arial", 12))
        lucro3.pack()
        bt3 = tkinter.Button(investir, text="Investir",command=lambda: roletarussa(lucro3),activebackground="#0DC016",font=(15))
        
        bt3.pack(pady=5)

def telaDosPobres(appbanco):

        anuncios = tkinter.Toplevel(appbanco)
        anuncios.resizable(False, False)
        anuncios.title("Anuncios")
        anuncios.geometry("600x500")
        appbanco.iconbitmap("Banco-Investimento--Trabalho-Rad/icone.ico")
        
        nome = tkinter.Label(anuncios, text = f"Bem-Vindo {usuario}\nSeu saldo: \n{Renda}",font=("Arial", 16))
        nome.pack()

        txt1 = tkinter.Label(anuncios, text = "Você não possui o necessario para investir \n mas sinta-se a vontade para ver nossos anuncios",font=("Arial",12), fg="#CE0F2F")
        txt1.pack() 

        ad1 = tkinter.Label(anuncios, text = "\nInvista na estacao de ca",font=("Arial",16, "bold"))
        ad1.pack() 

        ds1 = tkinter.Label(anuncios, text = "Vem pra ca do outro lado ",font=("Arial",12))
        ds1.pack()

        ad2 = tkinter.Label(anuncios, text = "\nInvista na mc ronalds",font=("Arial",16, "bold"))
        ad2.pack()
        
        ds2 = tkinter.Label(anuncios, text = "venha para o mac ronalds aqui nos temos \n um palhaço de 50 anos com cara de 10",font=("Arial",12))
        ds2.pack()

        ad3 = tkinter.Label(anuncios, text = "\nInvista na border king",font=("Arial",16, "bold"))
        ad3.pack()

        ds3 = tkinter.Label(anuncios, text = "é o restaurante que te faz atravessar fronteiras ",font=("Arial",12))
        ds3.pack()

        close = tkinter.Button(anuncios, text="Fechar", command=anuncios.destroy)
        close.pack

def cadstrar():
        try:
                global usuario
                global Renda
                usuario = (cadUsuario.get())
                Renda = (cadRenda.get()) 
                cursor.execute(f"INSERT INTO Banco(Usuario, Renda) VALUES('{usuario}', {Renda})")
        except:
                resultCad.config(text="Usuário ja existe",fg="#FA114F")

#01

appbanco = tkinter.Tk()
appbanco.title("Banco genial")
appbanco.resizable(False, False)
appbanco.geometry("600x500")
appbanco.iconify() 
appbanco.update()
appbanco.deiconify() 
appbanco.iconbitmap("Banco-Investimento--Trabalho-Rad/icone.ico")
 

#se nao fica igual
usuarioentrada = tkinter.StringVar()
rendaentrada = tkinter.StringVar()

espaco = tkinter.Label(appbanco, text = "")
espaco.pack(pady=14)

txt5 = tkinter.Label(appbanco, text = "--Entrar--",font=("Arial", 18))
txt5.pack(pady=10)

txt4 = tkinter.Label(appbanco, text = "Usuário")
txt4.pack()
entrada1 = tkinter.Entry(appbanco, textvariable=usuarioentrada,width=10,font=("Arial", 18))
entrada1.pack()

result = tkinter.Label(appbanco, text = "",font=("Arial", 16))
result.pack()

btn = tkinter.Button(appbanco, text="Entrar",command=Pesquisa,activebackground="#438BCF",width=5,font=(15))
btn.pack()


#se nao fica igual
cadUsuario = tkinter.StringVar()
cadRenda = tkinter.StringVar()

txt1 = tkinter.Label(appbanco, text = "--Cadastrar--",font=("Arial", 18))
txt1.pack(pady=10)

txt2 = tkinter.Label(appbanco, text = "Usuário")
txt2.pack()
entrada2 = tkinter.Entry(appbanco, textvariable=cadUsuario,width=10,font=("Arial", 18))
entrada2.pack()

txt3 = tkinter.Label(appbanco, text = "Renda")
txt3.pack()
entrada3 = tkinter.Entry(appbanco, textvariable=cadRenda,width=10,font=("Arial", 18))
entrada3.pack()

resultCad = tkinter.Label(appbanco, text = "",font=("Arial", 16))
resultCad.pack()

btn2 = tkinter.Button(appbanco, text="Cadastrar",command=cadstrar,activebackground="#438BCF",width=8, font=(15))
btn2.pack()


appbanco.mainloop()  #loop principal, impede o código de seguir e permite capturar inputs



conectar.commit()

conectar.close()