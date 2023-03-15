import os

import pyautogui as p

local = os.path.dirname(os.path.realpath(__file__))

x, y = 36, 200

p.doubleClick(x, y)
p.sleep(1)
p.getActiveWindow().maximize()  # type:ignore
p.write('www.udemy.com')
p.press('enter')
p.sleep(10)

img_pesq = local+"\\pesquisa.png"
local_pesq = p.locateOnScreen(img_pesq,  confidence=.7)
x, y = p.center(local_pesq)  # type:ignore
p.moveTo(x, y)
p.click(x, y)
p.sleep(3)
p.write('Charles Lima')
p.press('enter')
p.sleep(4)
img_close = local+"\\close.png"
local_pesq = p.locateOnScreen(img_close,  confidence=.7)
x, y = p.center(local_pesq)  # type:ignore
p.moveTo(x, y)
p.click(x, y)
