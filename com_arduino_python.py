import serial
import threading
import tkinter as tk

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        label = tk.Label(self.root, text="Hello Walter")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        canvas = tk.Canvas(self.root, width=1080, height=720, background="RoyalBlue4") 
        canvas.pack()
        
        def rectanglef(dim):
            canvas.create_rectangle(dim, outline="black", fill="white") 
        def rectangled(dim):
            canvas.create_rectangle(dim, outline="black", fill="yellow")
        
        rectanglef([330, 240, 360, 500])##pouce full
        rectanglef([400, 80, 430, 500])##index full
        rectanglef([480, 40, 510, 500])##majeur full
        rectanglef([560, 80, 590, 500])##annulaire full
        rectanglef([630, 240, 660, 500])##auriculaire full

        rectangled([330, 360, 360, 500])##pouce demi
        rectangled([400, 240, 430, 500])##index demi
        rectangled([480, 160, 510, 500])##majeur demi
        rectangled([560, 240, 590, 500])##annulaire demi
        rectangled([630, 360, 660, 500])##auriculaire demi

        canvas.create_oval(320,340,700,600,fill='red')##paume main

        label.pack()
        self.root.mainloop()

def task():
   # do something
	self.root.update()

app = App()
try:
    arduino = serial.Serial("COM3", timeout=1)
except:
    print("Please check the port")
count = 0
down1 = 0
down2 = 0
down3 = 0
down4 = 0
down5 = 0
rawdata = []
while count >= 0:
    count+=1
    res = str(arduino.readline())
    if ("1" in res):
        down1+=1
    if ("11" in res):
        down1 = 0
    if ("2" in res):
        down2+=1
    if ("12" in res):
        down2 = 0
    if ("3" in res):
        down3+=1
    if ("13" in res):
        down3 = 0
    if ("4" in res):
        down4+=1
    if ("14" in res):
        down4 = 0
    if ("5" in res):
        down5+=1
    if ("15" in res):
        down5 = 0
    if (down1 >= 3):
        print("DOWN1")
    else:
        print("UP1")
    if (down2 >= 3):
        print("DOWN2")
    else:
        print("UP2")
    if (down3 >= 3):
        print("DOWN3")
    else:
        print("UP3")
    if (down4 >= 3):
        print("DOWN4")
    else:
        print("UP4")
    if (down5 >= 3):
        #rectanglef([330, 240, 360, 500])##pouce full
        print("DOWN5")
    else:
        print("UP5")