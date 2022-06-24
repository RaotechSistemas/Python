import pyautogui
import pyperclip
import time
import datetime
from datetime import datetime, timedelta, date

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
pyautogui.alert('Não toque no teclado/mouse durante a execução desse código!')
pyautogui.PAUSE= 1
data = date.today() - timedelta (1)
ontem = data.strftime('%d%m%Y')
url = "https://autoatendimento.bb.com.br/apf-apj-acesso/#/transacao/acesso-gerenciador-financeiro"
navegador = webdriver.Firefox()
navegador.get (url)
pyautogui.moveTo(x=760, y=350)
time.sleep (60)

pyautogui.click(x=760, y=350)
pyautogui.click(x=750, y=350)
pyautogui.write("JC206929")
pyautogui.moveTo(x=760, y=485)
pyautogui.click()
pyautogui.moveTo(x=750, y=515)
pyautogui.click()
pyautogui.write("C4l1c4r7")
pyautogui.moveTo(x=750, y=605)
pyautogui.click()
pyautogui.moveTo(x=200, y= 115)
time.sleep (30)
#2º Passo - Navegar pelo site do BB e extrair o movimento do dia anterior
pyautogui.click()
pyautogui.write ("Movimento do Dia")
pyautogui.click(x=200, y=200)


pyautogui.moveTo(x=1356, y=718)
pyautogui.click(x=1356, y=718)
pyautogui.click(x=1356, y=718)
pyautogui.click(x=1356, y=718) # Rolar tela

pyautogui.moveTo(x=341, y=430)
pyautogui.click(x=341, y=430)
pyautogui.write("20931") # Agencia

pyautogui.moveTo(x=341, y=480)
pyautogui.click(x=341, y=480)
pyautogui.write("26670") # Beneficiário

pyautogui.moveTo(x=341, y=526)
pyautogui.click(x=341, y=526)
pyautogui.write("17") # Carteira

pyautogui.moveTo(x=341, y=575)
pyautogui.click(x=341, y=575)
pyautogui.write("019") # Variação

pyautogui.moveTo(x=341, y=626)
pyautogui.click(x=341, y=626)
pyautogui.write (ontem) # Data do movimento

pyautogui.moveTo(x=183, y=687)
pyautogui.click(x=183, y=687) # Botão OK

pyautogui.moveTo(x=1354, y=297)
pyautogui.mouseDown()
pyautogui.moveTo(x=1357, y=119)
pyautogui.moveTo(x=1359, y=530)
pyautogui.mouseUp()

#CORRIGIR A PARTIR DAQUI
'''
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)
pyautogui.click(x=1359, y=720)

pyautogui.moveTo(x=282, y=684)
pyautogui.click(x=282, y=684)

pyautogui.hotkey('ctrl','p')
pyautogui.moveTo(x=989, y=660)
pyautogui.click(x=989, y=660)
pyautogui.moveTo(x=354, y=51)
pyautogui.write('Downloads')
pyautogui.press('enter')
pyautogui.moveTo(x=150, y=377)
pyautogui.write('movimento dia ',ontem)
pyautogui.press('enter')
time.sleep(10)
pyautogui.moveTo(x=1324, y=111)
pyautogui.click(x=1324, y=111)
time.sleep(20)
pyautogui.moveTo(x=1343, y=24)
pyautogui.click(x=1343, y=24)'''

pyautogui.alert('Seu código foi executado! Já pode usar o teclado/mouse novamente.')