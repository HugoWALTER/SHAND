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
##try:
##    arduino = serial.Serial("COM16", timeout=1)
##except:
##    print("Please check the port")
##count = 0
##down = 0
##up = 0
##rawdata = []
##while count >= 0:
##    count+=1
##    res = str(arduino.readline())
##    if ("0" in res):
##        down+=1
##        up = 0
##    if ("1" in res):
##        down = 0
##        up+=1
##    if (up >= 5):
##        up = 0
##        print("UP")
##    if (down >= 5):
##        down = 0
##        print("DOWN")