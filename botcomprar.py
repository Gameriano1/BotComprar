import time
import cv2 as cv
import subprocess
import pydirectinput
from mss import mss
import pytesseract
import ctypes
import reembolso
import pyautogui
import mss.tools as mss_tools

def abrirroblox(name):
    lnk_path = fr'C:\Users\{name}\Desktop\Roblox.lnk'
    subprocess.call(lnk_path, shell=True)

class BotComprar():
    def printar():
        with mss() as sct:
                global shot
                global bbox
                hwnd = ctypes.windll.user32.FindWindowW(0, 'Roblox')
                rect = ctypes.wintypes.RECT()
                ctypes.windll.user32.GetWindowRect(hwnd, ctypes.pointer(rect))
                monitor = sct.monitors[1]

                bbox = (rect.left+5, rect.top, rect.right-7, rect.bottom-7)
                shot = sct.grab(bbox)
                mss_tools.to_png(shot.rgb, shot.size, output=fr'imgs\robuxaparecer.png')

    def IA(fundo,objeto):
        global max_loc
        global concluido_w
        global concluido_h
        global existe
        variavel = cv.imread(f'imgs\{fundo}',cv.IMREAD_ANYCOLOR)
        numero = cv.imread(f'imgs\{objeto}',cv.IMREAD_ANYCOLOR)
        result = cv.matchTemplate(variavel,numero,cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val >= 0.95:
            existe = 'sim'
            concluido_w = numero.shape[1]
            concluido_h = numero.shape[0]

            top_left = max_loc
            bottom_right = (top_left[0] + concluido_w, top_left[1] + concluido_h)

            cv.rectangle(variavel, top_left, bottom_right,
            color=(0, 0, 255), thickness=3, lineType=cv.LINE_4)
            # cv.imshow('eae', variavel)
            # cv.waitKey()
        else:
            existe = 'nao'

    def clicar():
        pydirectinput.click(
            x=max_loc[0] + concluido_w//2 + bbox[0],
            y=max_loc[1] + concluido_h//2 + bbox[1],
            duration=0.5
        )

    def getrobuxlist():
        time.sleep(1)
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'robux.png')
        while existe == 'nao':
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'robux.png')
        BotComprar.clicar()
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'saldo.png')
        while existe == 'nao':
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'saldo.png')

    def comprar(premium , qual, senhas, endereco=True):
        def comprar88():
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', '88.png')
            if existe == 'sim':
                BotComprar.clicar()
        if premium:
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', '450.png')
            if existe == 'sim':
                BotComprar.clicar()
        if not premium:
            comprar88()

        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'senha.png')
        while not existe == 'sim':
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'senha.png')
        BotComprar.clicar()

        senha = senhas[0]
        print(senha)

        pyautogui.write(senha)
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'entrar.png')
        if existe == "sim":
            BotComprar.clicar()

        if endereco:
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'endereco.png')
            while not existe == "sim":
                BotComprar.printar()
                BotComprar.IA('robuxaparecer.png', 'endereco.png')
            BotComprar.clicar()
            time.sleep(4)
            pyautogui.write('asdhsahdhas')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.write('Dover')
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'selecionar.png')
            BotComprar.clicar()
            time.sleep(1)
            pyautogui.write('d')
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.scroll(-50)
            time.sleep(2)
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'cep.png')
            BotComprar.clicar()
            pyautogui.write('19904')
            time.sleep(1)
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'salvar.png')
            BotComprar.clicar()
            BotComprar.printar()
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'alterar.png')
            while not existe == "sim":
                BotComprar.printar()
                BotComprar.IA('robuxaparecer.png', 'alterar.png')
            BotComprar.IA('robuxaparecer.png', 'usar.png')
            BotComprar.clicar()
        pydirectinput.moveTo(0, 500)
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'pp.png')
        while not existe == "sim":
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'pp.png')
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'comprar.png')
        while not existe == 'sim':
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'comprar.png')
        BotComprar.clicar()
        BotComprar.printar()
        BotComprar.IA('robuxaparecer.png', 'fechar.png')
        while not existe == 'sim':
            BotComprar.printar()
            BotComprar.IA('robuxaparecer.png', 'fechar.png')
        BotComprar.clicar()

def reembolsoo(qual, senhas):
    reembolso.xbox(qual[0], senhas[0])


