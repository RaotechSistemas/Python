import pyautogui
import pyperclip
import time
pyautogui.alert('Não toque no teclado/mouse durante a execução desse código!')
pyautogui.PAUSE = 1
#pyautogui.KEYBOARD_KEYS
pyautogui.press('winright')
pyautogui.write('firefox')
pyautogui.press ('enter')

'''
pyautogui.mouseDown()
pyautogui.mouseUp()'''

time.sleep (4)
pyautogui.moveTo(259, 52)
pyperclip.copy('https://autoatendimento.bb.com.br/apf-apj-acesso/#/transacao/acesso-gerenciador-financeiro/0')
pyautogui.hotkey('ctrl','v')
pyautogui.press ('enter')
time.sleep (6)
#pyautogui.moveTo(842,358)
pyautogui.click(x=762, y=354)
pyautogui.click(x=762, y=354)
pyautogui.write("JC206929")
pyautogui.click(x=796, y=462)
# Passo 02. No Firefox, digitar na barra de navegação "bb.com.br"

# Passo 03. 

pyautogui.alert('Seu código foi executado! Já pode usar o teclado/mouse novamente.')