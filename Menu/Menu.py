from PySimpleGUI import PySimpleGUI as sg 

import mysql.connector    

from decouple import config

from datetime import datetime

import socket

# Criando layout
def janela_menu():
 sg.theme('Material1')

layoutMenu = [
        [sg.Text('\n       MENU SUPERMERCADO', size=(26,3))],
        [sg.Button('Efetuar compra', size=(25,1))],
        [sg.Button('Cadastrar produtos', size=(25,1))],
        [sg.Text('\n')]
]
janelaMenu = sg.Window('Cadastro de produtos', layoutMenu)

while True:
    
    import mysql.connector
    
    eventoMenu, menu = janelaMenu.read()
    if eventoMenu == sg.WINDOW_CLOSED:
        break
    
    
    
    #-------------------CADASTRAR PRODUTOS------------------------#
    if eventoMenu == 'Cadastrar produtos':
        layoutCadastro = [
        [sg.Text('Produto'), sg.Input(key='Item', size=(23,1))],
        [sg.Text('Codigo'), sg.Input(key='Código', size=(24,1))],
        [sg.Text('Valor'), sg.Input(key='Valor', size=(25,1))],
        [sg.Text('Quantidade'), sg.Input(key='Qntd', size=(20,1))],
        [sg.Checkbox('Item em estoque', key="Check")], 
        [sg.Button('Cadastrar Produto', size=(27,1))],
        [sg.Button('Cancelar Cadastro', size=(27,1))]
        ]
        JanelaCadastro = sg.Window('Cadastro de produtos', layoutCadastro)
        
        eventoCadastro, cadastro = JanelaCadastro.read()
        if eventoCadastro == sg.WINDOW_CLOSED:
            break
        
        if eventoCadastro == 'Cancelar Cadastro':
            sg.popup('O cadastro foi cancelada')
            break
        
        if eventoCadastro == 'Cadastrar Produto':
        
            Produto = cadastro['Item']
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
        (data, IP, Produto, Valor, código, Qntd, Check)
        ]
        cursor.executemany(sql, value)
        myconnection.commit()
        print(cursor.rowcount, "Registro inserido")

        #Fechando conexão
        myconnection.is_connected() 
        cursor.close()
        myconnection.close()
        sg.popup('Produto cadastrado com sucesso')
        break
    
        
    
    
    #-------------------------EFETUAR COMPRA-------------------------#
    if eventoMenu == 'Efetuar compra':
        layoutCompra = [
        [sg.Text('Item'), sg.Input(key='Item', size=(20,1))],
        [sg.Text('Valor do item'), sg.Input(key='Valor do item', size=(20,1))],
        [sg.Checkbox('Cartão de crédito', key='CheckCC')],
        [sg.Checkbox('Cartão de débito', key='CheckCD')],
        [sg.Checkbox('Dinheiro', key="CheckD")],
        [sg.Button('Processar Pagamento')],
        [sg.Button('Cancelar Compra')]
        ]

        janelaCompra = sg.Window('Pagamento', layoutCompra)
        
        eventoCompra, compra = janelaCompra.read()
        if eventoCompra == sg.WINDOW_CLOSED:
            break
        
        if eventoCompra == 'Processar Pagamento':
            
            #Pegando os Inputs e colocando em variaveis
            item = compra['Item']
            valor = compra['Valor do item']
            CC = compra['CheckCC']
            CD = compra['CheckCD']
            D = compra['CheckD']
            data = datetime.now()
            IP = socket.gethostbyname(socket.gethostname())
            
            #Criando conexão com o banco de dados e inserindo os inputs
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
        
        #Condição para cancelar compra
        if eventoCompra == 'Cancelar Compra':
            sg.popup('A compra foi cancelada')
            break