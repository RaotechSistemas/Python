import pyautogui
import time

pyautogui.PAUSE = 1
# Criando um novo arquivo Excel')
pyautogui.moveTo(450,450)
pyautogui.hotkey('winleft')
pyautogui.write('excel')
pyautogui.press('enter')
time.sleep (60)
pyautogui.moveTo(265, 210)
pyautogui.click()

# Abrindo o arquivo de texto na Area de Trabalho')
time.sleep(5)
pyautogui.moveTo(450, 50) # Dados
pyautogui.click()
time.sleep(5)
pyautogui.moveTo(110, 80) # De Text/CSV
pyautogui.click()
time.sleep(15)
pyautogui.moveTo(80, 175) # Área de Trabalho
pyautogui.click(80,175)
time.sleep(5)
pyautogui.moveTo(255, 145) # Arquivo .txt
pyautogui.doubleClick(255, 145)
time.sleep (15)
pyautogui.moveTo(745, 100) # Maximizar tela
pyautogui.doubleClick(745, 200)
pyautogui.moveTo(345, 90)
pyautogui.click(345, 90)
pyautogui.moveTo(307, 212) # Tabulação
pyautogui.click(307, 212)
time.sleep (10)

pyautogui.moveTo(1088, 688) # Carregar
pyautogui.click()
time.sleep (10)

pyautogui.moveTo(1340, 225) # Fechar Consultas e Conexões
pyautogui.click()
pyautogui.moveTo(865, 215) # Selecionar coluna "H"
pyautogui.rightClick(865, 215) # Clique botão direito do mouse
pyautogui.moveTo(910, 375) # Excluir Coluna "H"
pyautogui.click()

pyautogui.moveTo(1125, 215) # Selecionar coluna "K"
pyautogui.rightClick(1125, 215) # Clique botão direito do mouse
pyautogui.moveTo(1185, 375) # Excluir Coluna "K"
pyautogui.click()

pyautogui.moveTo(1110, 215) # Selecionar coluna "K" de novo
pyautogui.rightClick(1110, 215) # Clique botão direito do mouse
pyautogui.moveTo(1170, 375) # Excluir Coluna "K" de novo
pyautogui.click()

pyautogui.moveTo(1125, 215) # Selecionar coluna "K" até a ultima
pyautogui.click()
pyautogui.hotkey('ctrl','shift','right')
pyautogui.rightClick()
pyautogui.moveTo(1195, 470) # Ocultar 
pyautogui.click()
pyautogui.moveTo(80, 210)
pyautogui.mouseDown()
pyautogui.hotkey('ctrl','shift','right')
pyautogui.moveTo(410, 120)
pyautogui.click(410, 120)
pyautogui.moveTo(860, 215) # Selecionar coluna "H"
pyautogui.doubleClick(860,215) 
pyautogui.moveTo(1180, 100) # Localizar e Selecionar
pyautogui.click()
pyautogui.moveTo(1205, 175) # Substituir
pyautogui.click()
pyautogui.moveTo(610, 305)
pyautogui.doubleClick(610, 305) # Maximizar Tela
pyautogui.moveTo(140, 75)
pyautogui.click() 
pyautogui.write (' ') # Excluir espaçõs vazios na coluna "H"
pyautogui.moveTo(900, 220)
pyautogui.click()
pyautogui.press('enter')
pyautogui.moveTo(1320, 220)
pyautogui.click()
pyautogui.alert ('Geração de relatório concluído!')

