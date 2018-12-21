import serial
import threading
import tkinter as tk
import sys

def rectanglef(canvas, dim):
    canvas.create_rectangle(dim, outline="black", fill="white")

def rectangled(canvas, dim):
    canvas.create_rectangle(dim, outline="black", fill="yellow")

def rectangler(canvas, dim):
    canvas.create_rectangle(dim, outline="RoyalBlue4", fill="RoyalBlue4")

root = tk.Tk()
root.title("SHAND")
label = tk.Label(root, text="Left Hand")
canvas = tk.Canvas(root, width=1080, height=720, background="RoyalBlue4") 
canvas.pack()
label.pack()

def callback():
    root.destroy()

try:
    arduino = serial.Serial("COM16", timeout=1)
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
    root.protocol("WM_DELETE_WINDOW", callback)
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
        rectangler(canvas, [630, 360, 660, 500])##reset auriculaire demi
        rectanglef(canvas, [630, 240, 660, 500])##auriculaire full
        #print("DOWN1")
    else:
        rectangler(canvas, [630, 240, 660, 500])##reset auriculaire full
        rectangled(canvas, [630, 360, 660, 500])##auriculaire demi
        #print("UP1")
    if (down2 >= 3):
        rectangler(canvas, [560, 240, 590, 500])##reset annulaire demi
        rectanglef(canvas, [560, 80, 590, 500])##annulaire full
        #print("DOWN2")
    else:
        rectangler(canvas, [560, 80, 590, 500])##reset annulaire full
        rectangled(canvas, [560, 240, 590, 500])##annulaire demi
        #print("UP2")
    if (down3 >= 3):
        rectangler(canvas, [480, 160, 510, 500])##reset majeur demi
        rectanglef(canvas, [480, 40, 510, 500])##majeur full
        #print("DOWN3")
    else:
        rectangler(canvas, [480, 40, 510, 500])##reset majeur full
        rectangled(canvas, [480, 160, 510, 500])##majeur demi
        #print("UP3")
    if (down4 >= 3):
        rectangler(canvas, [400, 240, 430, 500])##reset index demi
        rectanglef(canvas, [400, 80, 430, 500])##index full
        #print("DOWN4")
    else:
        rectangler(canvas, [400, 80, 430, 500])##reset index full
        rectangled(canvas, [400, 240, 430, 500])##index demi
        #print("UP4")
    if (down5 >= 3):
        rectangler(canvas, [330, 360, 360, 500])##reset pouce demi
        rectanglef(canvas, [330, 240, 360, 500])##pouce full
        #print("DOWN5")
    else:
        rectangler(canvas, [330, 240, 360, 500])##reset pouce full
        rectangled(canvas, [330, 360, 360, 500])##pouce demi
        #print("UP5")
    canvas.create_oval(320,340,700,600,fill='red')##paume main
    root.update()
root.mainloop()


##rectanglef(canvas, [330, 240, 360, 500])##pouce full
##rectanglef(canvas, [400, 80, 430, 500])##index full
##rectanglef(canvas, [480, 40, 510, 500])##majeur full
##rectanglef(canvas, [560, 80, 590, 500])##annulaire full
##rectanglef(canvas, [630, 240, 660, 500])##auriculaire full

##rectangled(canvas, [330, 360, 360, 500])##pouce demi
##rectangled(canvas, [400, 240, 430, 500])##index demi
##rectangled(canvas, [480, 160, 510, 500])##majeur demi
##rectangled(canvas, [560, 240, 590, 500])##annulaire demi
##rectangled(canvas, [630, 360, 660, 500])##auriculaire demi