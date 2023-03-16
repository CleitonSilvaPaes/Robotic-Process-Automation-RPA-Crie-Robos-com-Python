import os as o

import pandas as pd
import pyautogui as p
import rpa as r

r.init(turbo_mode=True)
r.url('https://rpachallengeocr.azurewebsites.net/')
janela = p.getActiveWindow().maximize()  # type:ignore
p.sleep(7)

countPage = 1
while countPage <= 3:
    if countPage == 1:
        r.table('//*[@id="tableSandbox"]', 'temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=True)  # type:ignore # noqa
        r.click('//*[@id="tableSandbox_next"]')
    else:
        r.table('//*[@id="tableSandbox"]', 'temp.csv')
        dados = pd.read_csv('Temp.csv')
        dados.to_csv(r'WebTable.csv', mode='a', index=None, header=False)  # type:ignore # noqa
        r.click('//*[@id="tableSandbox_next"]')
    countPage += 1
r.close()
o.remove('Temp.csv')