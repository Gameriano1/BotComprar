from botcomprar import BotComprar,abrirroblox, reembolsoo
import os
from colorama import Fore
from colorama import Style
import json
import PySimpleGUI as sg

def guimain():
    global listafinal
    global robux
    global premium
    global endereco
    listafinal = []
    for conta, sen in zip(emails, senhas):
        lista = str(conta + ':' + sen + '\n')
        listafinal.append(lista)

    premium = False
    endereco = False
    sg.theme('DarkAmber')
    layout = [[sg.Text("Bem vindo ao comprador de robux!", font=('Axial', 25), size=(25,3), text_color="Red")], [sg.Text("quantas vezes comprar robux", text_color="Red"), sg.InputText()],[sg.Button("Rodar", size=(25,4), button_color=("red", "White"))], [sg.Button("Visualizar contas:senhas", size=(25,4), button_color=("red",'white'))], [sg.Button("Configurações", size=(25,4), button_color=("red",'white'))] ,[sg.Text("Feito por Shad, shadzz#5571",text_color="Red")]]

    # Create the window
    window = sg.Window("Comprador De Robux", layout, margins=(100, 100))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Visualizar contas:senhas":
            gui2()
        if event == "Rodar":
            break
        if event == "Configurações":
            config()
        elif event == sg.WIN_CLOSED:
            exit()
    robux = int(values[0])
    window.close()

def gui2():
    global textx
    textx = ''.join(listafinal)
    layout = [[sg.Text("Emails         ||          Senhas" + '\n' + textx, key="new", font=('Axial',12), text_color="White")]]
    window = sg.Window("Second Window", layout, margins=(100, 100))
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def config():
    global premium
    global endereco
    layout = [[sg.Text("Configurações do Programa", key="new", font=('Axial', 12), text_color="White")], [sg.Checkbox('Comprar Premium?', key="amor", default=False, enable_events=True)], [sg.Checkbox('Usar Endereço', key="lari", default=False, enable_events=True)]]
    window2 = sg.Window("Thirty Window", layout, margins=(100, 100))
    while True:
        event, values2 = window2.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif values2["amor"] == True:
            premium = True
        elif values2["lari"] == True:
            endereco = True
    window2.close()

def main():
    global emails
    global senhas
    input_file = open('contas.json')
    data = json.load(input_file)

    emails = data['email']
    senhabase = data['senhas']
    i = -1
    for _ in senhabase:
        i += 1

    if len(senhabase) < len(emails):
        senhatotal = senhabase[i]
        senhas = []
        for item in senhabase:
            senhas.append(item)
        for i in range(len(emails)-i-1):
            senhafinal = senhas.append(senhatotal)

    guimain()
    if robux < 1:
        reembolsoo(qual=emails, senhas=senhas)
        exit()

    roblox = os.getenv('username')

    print(f"{Fore.RED}Lembre-se De colocar as contas no arquivo json.{Style.RESET_ALL}!")

    abrirroblox(name=roblox)
    BotComprar.getrobuxlist()
    if premium and endereco:
        BotComprar.comprar(senhas=senhas, qual=emails, premium=bool(premium), endereco=bool(endereco))
        for _ in range(int(robux-1)):
            BotComprar.comprar(senhas=senhas,qual=emails, premium=False, endereco=False)
    elif premium:
        BotComprar.comprar(senhas=senhas, qual=emails, premium=bool(premium))
        for _ in range(int(robux-1)):
            BotComprar.comprar(senhas=senhas, qual=emails, premium=False, endereco=False)
    elif endereco:
        BotComprar.comprar(senhas=senhas, qual=emails, premium=False)
        for _ in range(int(robux-1)):
            BotComprar.comprar(senhas=senhas, qual=emails, premium=False, endereco=False)
    else:
        for _ in range(int(robux)):
            BotComprar.comprar(senhas=senhas,qual=emails, premium=False, endereco=False)

    reembolsoo(qual=emails, senhas=senhas)

if __name__ == "__main__":
    main()