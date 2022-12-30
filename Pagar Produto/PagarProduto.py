# Importando biblioteca do PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg  

from datetime import datetime

import mysql.connector

from decouple import config

import socket



# Criando layout
def janela_pagamento_produtos():
 sg.theme('Material1')
layout = [
    [sg.Text('Item'), sg.Input(key='Item', size=(20,1))],
    [sg.Text('Valor do item'), sg.Input(key='Valor do item', size=(20,1))],
    [sg.Checkbox('Cartão de crédito', key='CheckCC')],
    [sg.Checkbox('Cartão de débito', key='CheckCD')],
    [sg.Checkbox('Dinheiro', key="CheckD")],
    [sg.Button('Processar Pagamento')],
    [sg.Button('Cancelar Compra')]
]

janela = sg.Window('Cadastro de produtos', layout)

# Ler os eventos e executalos
while True:
    
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Processar Pagamento':
        
        #Pegando os Inputs e colocando em variaveis
        item = valores['Item']
        valor = valores['Valor do item']
        CC = valores['CheckCC']
        CD = valores['CheckCD']
        D = valores['CheckD']
        data = datetime.now()
        IP = socket.gethostbyname(socket.gethostname())
        
        
        #Criando conexão e inserindo os inputs
        myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
    
        cursor = myconnection.cursor()
        sql = "INSERT INTO HistoricoCompras (Horario, IP, item, valor, CC, CD, D) VALUE (%s, %s, %s, %s, %s, %s, %s)"
        value = [
        (data, IP, item, valor, CC, CD, D)
        ]
        cursor.executemany(sql, value)
        myconnection.commit()
        print(cursor.rowcount, "Registro inserido")

        myconnection.is_connected() 
        cursor.close()
        myconnection.close()
        print("Conexao ao MySql foi encerrada")
        
        sg.popup('O pagamento foi efetuado com sucesso')
        break
    
    if eventos == 'Cancelar Compra':
        sg.popup('A compra foi cancelada')
        break
    
    
    
    
    
