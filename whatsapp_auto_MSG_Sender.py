import pyautogui
import time

m = input("Enter your MSG :  ")
t = int(input("how many Times you want to send : "))
c = 0
time.sleep(5)
while c<t:

    pyautogui.typewrite(m)
    pyautogui.press("enter")

    c = c+1
