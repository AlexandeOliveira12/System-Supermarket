# Importando biblioteca do PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg  
    
# Criando layout
def janela_cadastro_produtos():
 sg.theme('Material1')
layout2 = [
    [sg.Text('Item'), sg.Input(key='Item', size=(20,1))],
    [sg.Text('Código do item'), sg.Input(key='Código do item', size=(20,1))],
    [sg.Text('Valor do item'), sg.Input(key='Valor do item', size=(20,1))],
    [sg.Checkbox('Salvar item no banco de dados')], 
    [sg.Button('Cadastrar Produto')]
]

janela2 = sg.Window('Cadastro de produtos', layout2)

# Ler os eventos e executalos
while True:
    eventos, valores = janela2.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    
    if eventos == 'Cadastrar Produto':
        sg.popup('Produto cadastrado com sucesso')
        break
    