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

        label.pack()

        self.root.mainloop()

def task():
   # do something
   root.update()

app = App()
try:
    arduino = serial.Serial("COM3", timeout=1)
except:
    print("Please check the port")
count = 0
down = 0
up = 0
rawdata = []
while count >= 0:
    count+=1
    res = str(arduino.readline())
    if ("0" in res):
        down+=1
        up = 0
    if ("1" in res):
        down = 0
        up+=1
    if (up >= 5):
        up = 0
        print("UP")
    if (down >= 5):
        down = 0
        print("DOWN")