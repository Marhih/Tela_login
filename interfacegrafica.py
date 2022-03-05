from PySimpleGUI import PySimpleGUI as sg

sg.theme('LightBlue')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
telaerro = [
    [sg.Text('Usuário ou Senha incorretos!')]
]
bemvinda = [
    [sg.Text('Bem Vindo!')]
]
janela = sg.Window('Tela de Login', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'usuario'.strip() and valores['senha'] == '12345':
            jan = sg.Window('Login', bemvinda)
            eventos, valores = jan.read()
        elif valores['usuario'] != 'usuario'.strip() or valores['senha'] != '12345':
            janelaaa = sg.Window('ERRO', telaerro)
            eventos, valores = janelaaa.read()
