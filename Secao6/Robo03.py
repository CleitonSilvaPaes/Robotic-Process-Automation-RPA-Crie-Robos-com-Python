import rpa as r
import pyautogui as p
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import dotenv_values

config = dotenv_values('.env')


r.init(turbo_mode=True)
p.getActiveWindow().maximize()  # type:ignore
r.url('https://www.melhorcambio.com/dolar-hoje')
p.sleep(5)
dolar_comercial = r.read('//*[@id="comercial"]')
r.close()

texto_email = f'{dolar_comercial} Hoje: {pd.Timestamp("today")}'

# email remetente, senha, destinatário
de = 'cleitonsilvacarvalhopaes@gmail.com'
para = 'cleitonsilvacarvalhopaes@gmail.com'
senha = config["SENHA"]

# Setup the MIME
messagem = MIMEMultipart()
messagem['From'] = de
messagem['To'] = para
messagem['Subject'] = 'Cotacao do dolar'

# Corpo do E-mail com anexos
messagem.attach(MIMEText(texto_email, 'plain'))

# Criando sessao SMTP com o email
session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(de, senha)  # type:ignore
texto = messagem.as_string()
session.sendmail(de, para, texto)
session.quit()
