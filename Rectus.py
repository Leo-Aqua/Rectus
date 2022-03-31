
import win32gui, win32api, keyboard, random, time #imports
print("""
8888888b.  8888888888  .d8888b.  88888888888 888     888  .d8888b.  
888   Y88b 888        d88P  Y88b     888     888     888 d88P  Y88b 
888    888 888        888    888     888     888     888 Y88b.      
888   d88P 8888888    888            888     888     888  "Y888b.   
8888888P"  888        888            888     888     888     "Y88b. 
888 T88b   888        888    888     888     888     888       "888 
888  T88b  888        Y88b  d88P     888     Y88b. .d88P Y88b  d88P 
888   T88b 8888888888  "Y8888P"      888      "Y88888P"   "Y8888P"  
""")


# prints logo
def f1():
    while True:
        try:
            dc = win32gui.GetDC(0)
            win32gui.Rectangle(dc, random.randint(1, 2000), random.randint(1, 2000), random.randint(1, 2000), random.randint(1, 2000))
            if keyboard.is_pressed("ü"): #leave blank if you don't want to make it exitable
                break
        except:
            True

f1()
while True: #keeps Terminal alive
    True
    time.sleep(5)
    break
