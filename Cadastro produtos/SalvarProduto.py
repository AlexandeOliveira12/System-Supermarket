
#Biblioteca Interface
from PySimpleGUI import PySimpleGUI as sg 

#Cria conexão com o Mysql
import mysql.connector    

#Esconder dados importantes
from decouple import config

#Biblioteca para Pegar data e hora
from datetime import datetime

#Biblioteca para pegar IP
import socket

# Criando layout
def janela_cadastro_produtos():
 sg.theme('Material1')
 
layout = [
    [sg.Text('Produto'), sg.Input(key='Item', size=(20,1))],
    [sg.Text('Codigo'), sg.Input(key='Código', size=(20,1))],
    [sg.Text('Valor'), sg.Input(key='Valor', size=(20,1))],
    [sg.Text('Quantidade'), sg.Input(key='Qntd', size=(15,1))],
    [sg.Checkbox('Item em estoque', key="Check")], 
    [sg.Button('Cadastrar Produto')]
]
janela = sg.Window('Cadastro de produtos', layout)

# Ler os eventos e executalos
while True:
    
    import mysql.connector
    
    eventos, cadastro = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Cadastrar Produto':
        
        item = cadastro['Item']
        código = cadastro['Código']
        Valor = cadastro['Valor']
        Qntd = cadastro['Qntd']
        Check = cadastro['Check']
        data = datetime.now()
        IP = socket.gethostbyname(socket.gethostname())

        #Criando conexão e inserindo dados
        myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
    
        cursor = myconnection.cursor()
        sql = "INSERT INTO Produtos (Horario, IP, Nome, valor, Código, Qntd, ItemEmEstoque) VALUE (%s, %s, %s, %s, %s, %s, %s)"
        value = [
        (data, IP, item, Valor, código, Qntd, Check)
        ]
        cursor.executemany(sql, value)
        myconnection.commit()
        print(cursor.rowcount, "Registro inserido")

        #Fechando conexão
        myconnection.is_connected() 
        cursor.close()
        myconnection.close()
        print("Conexao ao MySql foi encerrada")
        print(f'{item}, {código}, {Valor}, {Qntd}, {Check}')
        sg.popup('Produto cadastrado com sucesso')
        break   
