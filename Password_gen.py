import random
import PySimpleGUI as sg
import os


class PassGen:
    def __init__(self):

        # Create Layout

        sg.theme('Black')
        layout = [
            [sg.Text('Site/Software', size=(10, 1)),
             sg.Input(key='site', size=(20, 1))],
            [sg.Text('E-mail/Usuário', size=(10, 1)),
             sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Quantidade de caracteres'), sg.Combo(values=list(range(30)),
             key='total_chars', default_value=1, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')]
        ]

        # Create Window
        self.window = sg.Window('Password Generator', layout)

    def start(self):
        while True:
            event, values = self.window.Read()
            if event == sg.WIN_CLOSED:
                break
            if event == 'Gerar Senha':
                new_password = self.generate_password(values)
                print(new_password)
                self.save_password(new_password, values)

    def generate_password(self, values):
        char_list = 'ABCDEFGHIJKLMNOPQRSTUVXZYWabcdefghijklmnopqrstuvxzyw1234567890!@#$%*'
        chars = random.choices(char_list, k=int(values['total_chars']))
        new_pass = ''.join(chars)
        return new_pass

    def save_password(self, new_password, values):
        with open('senhas.txt', 'a',newline='') as arquivo:
            arquivo.write(f"site: {values['site']}, usuario: {values['usuario']}, nova senha: {new_password}")
        print('Arquivo Salvo')


gen = PassGen()
gen.start()
