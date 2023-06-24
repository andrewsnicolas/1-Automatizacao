import pyautogui
import time
pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press("enter")
time.sleep(1)
for i in range(1, 100, 1):
    pyautogui.write("Eu amo minha mãe")
    pyautogui.press('enter')