# Importando biblioteca do PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg  
    
# Criando layout
def janela_pagamento_produtos():
 sg.theme('Material1')
layout = [
    [sg.Text('Item'), sg.Input(key='Item', size=(20,1))],
    [sg.Text('Valor do item'), sg.Input(key='Valor do item', size=(20,1))],
    [sg.Checkbox('Cartão de crédito')],[sg.Checkbox('Cartão de débito')],[sg.Checkbox('Dinheiro')],
    [sg.Button('Processar Pagamento')]
]

janela = sg.Window('Cadastro de produtos', layout)

# Ler os eventos e executalos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Processar Pagamento':
        sg.popup('O pagamento foi efetuado com sucesso')
        print(valores)
        break
    
    
    
    
    
