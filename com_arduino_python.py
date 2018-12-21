import serial
import threading
import tkinter as tk

class App(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def rectanglef(self, dim):
        self.canvas.create_rectangle(dim, outline="black", fill="white") 
    def rectangled(self, dim):
        self.canvas.create_rectangle(dim, outline="black", fill="yellow")
    def rectangler(self, dim):
        self.canvas.create_rectangle(dim, outline="RoyalBlue4", fill="RoyalBlue4")

    def run(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=1080, height=720, background="RoyalBlue4") 
        self.canvas.pack()
        label = tk.Label(self.root, text="Hello Walter")
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        
        #rectanglef([330, 240, 360, 500])##pouce full
        #rectanglef([400, 80, 430, 500])##index full
        #rectanglef([480, 40, 510, 500])##majeur full
        #rectanglef([560, 80, 590, 500])##annulaire full
        #rectanglef([630, 240, 660, 500])##auriculaire full
#
        #rectangled([330, 360, 360, 500])##pouce demi
        #rectangled([400, 240, 430, 500])##index demi
        #rectangled([480, 160, 510, 500])##majeur demi
        #rectangled([560, 240, 590, 500])##annulaire demi
        #rectangled([630, 360, 660, 500])##auriculaire demi

        self.canvas.create_oval(320,340,700,600,fill='red')##paume main

        label.pack()
        self.root.mainloop()

def task():
   # do something
	self.root.update()

try:
    arduino = serial.Serial("COM3", timeout=1)
except:
    print("Please check the port")
count = 0
down1 = 3
down2 = 3
down3 = 3
down4 = 3
down5 = 3
doigt1 = 0
doigt2 = 0
doigt3 = 0
doigt4 = 0
doigt5 = 0
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
    if (down1 < 3 and doigt1 == 0):
        print("ON Doigt 1")
        doigt1 = 1
    elif (down1 >= 3 and doigt1 == 1):
        doigt1 = 0
        print("OFF Doigt 1")
    if (down2 < 3 and doigt2 == 0):
        print("ON Doigt 2")
        doigt2 = 1
    elif (down2 >= 3 and doigt2 == 1):
        print("OFF Doigt 2")
        doigt2 = 0
    if (down3 < 3 and doigt3 == 0):
        print("ON Doigt 3")
        doigt3 = 1
    elif (down3 >= 3 and doigt3 == 1):
        print("OFF Doigt 3")
        doigt3 = 0
    if (down4 < 3 and doigt4 == 0):
        print("ON Doigt 4")
        doigt4 = 1
    elif (down4 >= 3 and doigt4 == 1):
        print("OFF Doigt 4")
        doigt4 = 0
    if (down5 < 3 and doigt5 == 0):
        print("ON Doigt 5")
        doigt5 = 1
    elif (down5 >= 3 and doigt5 == 1):
        print("OFF Doigt 5")
        doigt5 = 0