import pyautogui as pag
import pygetwindow as pgw
import pywinauto
import keyboard

#Activate LoL

win = pgw.getWindowsWithTitle('Discord')[0] #Switch to 'League of Legends'
if win.isActive == False:
    pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
win.activate()

#Click the chat

pag.click()

#Type in your line (Make radio buttons to select a line)

for i in range(5):
    keyboard.write(lines[line])
    pag.press('enter')

#Click the search bar on the screen + (Add a setting for selecting a resolution)

pag.click()

#Type in your champion's name

keyboard.write(champ_name)

#Lock in your champion

pag.click(win.left + 510, win.top + 980)    #Set to the search bar on the screen + (Add a setting for selecting a resolution)
keyboard.write(message)                     #Get the user to type the champion's name in
#pag.press('enter')