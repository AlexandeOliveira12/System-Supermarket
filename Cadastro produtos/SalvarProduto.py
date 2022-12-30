
# Importando biblioteca do PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg 

import mysql.connector    

from decouple import config

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
        print(f'{item}, {código}, {Valor}, {Qntd}, {Check}')
        sg.popup('Produto cadastrado com sucesso')
        break
    
    item = item
    código = código
    Valor = Valor
    Qntd = Qntd
    Check = Check   
      
myconnection = mysql.connector.connect(host=config("localhost"), user='root', password=config("password"), database=config("database"))
    
cursor = myconnection.cursor()
sql = "INSERT INTO Produtos (Nome, valor, Código, Qntd, ItemEmEstoque) VALUE (%s, %s, %s, %s, %s)"
value = [
(item, Valor, código, Qntd, Check)
]
cursor.executemany(sql, value)
myconnection.commit()
print(cursor.rowcount, "Registro inserido")

if myconnection.is_connected(): 
    cursor.close()
    myconnection.close()
    print("Conexao ao MySql foi encerrada")    

