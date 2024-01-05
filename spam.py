import pyautogui,time
time.sleep(5)
f=open("spam","YOU'VE BEEN HACKED")
for word in f:
  pyautogui.typewrite(word)
