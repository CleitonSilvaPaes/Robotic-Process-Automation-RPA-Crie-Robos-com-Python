"""
Baixando as bibliotecas

pyautogui
pandas
rpa
opencv-python

import pyautogui as p

Desse modo importamos o pyautogui

sleep() -> tempo para esperar para excutar uma funcao

position() -> Serve para pegar as possicao do mouse x, y

moveTo() -> Serve para depois que tiver a possicao do mouse para mover para o local designado. # noqa

click() -> dar um click no arquivo

doubleClick() -> Abrir arquivo

hotkey('win', 'r) -> Serve para tecla de atalho

typewrite -> Para escrever

press('enter') Serve para precionar uma tecla

getActiveWindow() -> Pega a janela atual do windows
getActiveWindow().close() -> Fecha a janela atual
"""

import pyautogui as p

# x, y = 40, 202

p.hotkey('win', 'r')
p.sleep(1)
p.typewrite('notepad')
p.sleep(1)
p.press('enter')
p.sleep(1)
p.typewrite('Oi!! Eu sou um Bot!')
p.sleep(1)
p.getActiveWindow().close() # noqa # type: ignore
p.sleep(1)
p.press('right')
p.sleep(0.5)
p.press('enter')
