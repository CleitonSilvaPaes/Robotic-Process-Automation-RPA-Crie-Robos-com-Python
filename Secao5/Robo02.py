"""
Site para informacao
>>> https://github-com.translate.goog/tebelorg/RPA-Python?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=en-US&_x_tr_pto=wapp # noqa

--------------------------------------------------------------------------------

init() -> Parametos
visual_automation=False, chrome_browser=True
iniciar TagUI, configuração automática na primeira execução

close()
fechar TagUI, navegador Chrome, SikuliX

pack()
para implantação de pacote sem internet

update()
para atualizar pacote sem internet

error()	-> Parametos True/False
definido como True para gerar exceção em caso de erro

debug()	-> Paramentos True/False/text_to_log
imprimir e registrar informações de depuração em rpa_python.log

type() -> Paramentos element_identifier(ou x, y), text( '[enter]'/ '[clear]')
digite o texto no elemento

wait() -> Parametos delay_in_seconds(padrão 5 segundos)
esperar explicitamente por algum tempo
"""
import rpa as r
import pyautogui as p

r.init()
r.url('http://www.google.com')
janala = p.getActiveWindow()  # type:ignore
p.sleep(1)
janala.maximize()
r.wait(2.0)
# r.type('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input', 'RPA[enter]') # noqa
r.type('//*[@name="q"]', 'RPA[enter]') # noqa
r.wait(2)
r.snap('page', 'rpa_page.png')
r.close()
