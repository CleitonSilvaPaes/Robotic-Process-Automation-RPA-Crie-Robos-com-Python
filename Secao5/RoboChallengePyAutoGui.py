import os

import pandas as pd
import pyautogui as p


def abrir_chrome(url):
    x, y = 27, 198
    p.doubleClick(x, y)
    p.sleep(1)
    p.getActiveWindow().maximize()  # type:ignore
    p.sleep(1)
    p.write(url)
    p.sleep(1)
    p.press('enter')
    p.sleep(3)


def download_challenge():
    local = os.path.dirname(os.path.realpath(__file__))
    arqs = os.scandir(local)
    arqs = [i.name for i in arqs]
    if 'challenge.xlsx' in arqs:
        pass
    else:
        x, y = 133, 657
        p.click(x, y)
        x, y = 610, 53
        p.sleep(1)
        p.click(x, y)
        x, y = 242, 250
        p.doubleClick(x, y)
        p.press('enter')


url = 'https://rpachallenge.com'
local = os.path.dirname(os.path.realpath(__file__)) + "\\img"
imagens = os.scandir(local)
nomes = [i.path for i in imagens]

abrir_chrome(url)
download_challenge()

df = pd.read_excel('challenge.xlsx')
df['Phone Number'] = df['Phone Number'].astype(str)

# Start

p.scroll(-50)
start = p.locateCenterOnScreen(nomes[8], confidence=.85)  # type:ignore
p.click(start.x, start.y)

for i in range(len(df.axes[0])):
    p.press('pagedown')
    for j in range(len(df.axes[1])):
        nome = df.axes[1][j]
        rodar = True
        img = None
        while rodar:
            try:
                img = p.locateCenterOnScreen(nomes[j], grayscale=True, confidence=.85, )  # type:ignore # noqa
                if img is not None:
                    rodar = False
            except Exception:
                pass
        print(nome)
        p.click(img)
        p.write(df[nome][i])
    img = p.locateCenterOnScreen(nomes[7], confidence=.85)  # type:ignore
    p.click(img.x, img.y)
