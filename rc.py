import pyautogui 
import time 
import numpy as np
pyautogui.FAILSAFE = False
 
#Ctrl + C = STOP
komen = input('Masukan Komentar mu: ')

while True:
    pyautogui.doubleClick(178,269)
    pyautogui.write((komen), interval=0.1)
    time.sleep(np.random.uniform(2,4))
    pyautogui.press('enter')
    time.sleep(np.random.uniform(3,7))
    




