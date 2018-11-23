import serial

try:
    arduino = serial.Serial("COM3", timeout=1)
except:
    print("Please check the port")

count = 0

file=open("data.txt",mode='w')
while count < 20:
    count+=1
    file.write(str(arduino.readline()) +'\n')

##def clean(L):#L is a list
##    newl=[]#initialising the new list
##    for i in range(len(L)):
##        temp=L[i][2:]
##        newl.append(temp[:-5])
##    return newl
##    
##
##def write(L):
##    file=open("data.txt",mode='w')
##    for i in range(len(L)):
##        file.write(L[i]+'\n')
##    file.close()
##
##write(cleandata)