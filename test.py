import pyautogui as pag
import pygetwindow as pgw
import keyboard
import time

print('start!')

#Get the coords of the current active window
while 1:
    if keyboard.read_key() == 'space':
        current_window = pgw.getActiveWindow()
        position = pag.position()
        print(position.x - current_window.left, position.y - current_window.top)
        time.sleep(0.3)  