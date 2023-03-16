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
    x, y = 133, 657
    p.click(x, y)
    x, y = 610, 53
    p.sleep(1)
    p.click(x, y)
    x, y = 301, 219
    p.doubleClick(x, y)
    p.press('right')
    p.sleep(1)
    p.press('enter')
    p.press('left')
    p.sleep(1)
    p.press('enter')
    p.sleep(1)
    # Start
    x, y = 150, 649
    p.scroll(-50)
    p.sleep(1)
    p.click(x, y)


url = 'https://rpachallenge.com'
local = os.path.dirname(os.path.realpath(__file__)) + "\\img"
imagens = os.scandir(local)
nomes = [i.path for i in imagens]

abrir_chrome(url)
download_challenge()

df = pd.read_excel('challenge.xlsx')
df['Phone Number'] = df['Phone Number'].astype(str)

for i in range(len(df.axes[0])):
    p.scroll(-70)
    for j in range(len(df.axes[1])):
        nome = df.axes[1][j]
        img = p.locateCenterOnScreen(nomes[j], confidence=.8)  # type:ignore
        print(nome)
        p.click(img)
        p.write(df[nome][i])
    img = p.locateCenterOnScreen(nomes[7], confidence=.8)  # type:ignore
    p.click(img.x, img.y)
