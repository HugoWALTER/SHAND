# SHAND 
> The first innovation project in EPITECH. 🆕 🎉.<br>

> This project was made in python and arduino with <3 by Hugo WALTER and Kevin FERCHAUD
 
## What is it?

SHAND is a connected gloves able to play jankenpon against and AI.<br>
 
**Current features:**

- Launching a graphical window to play against an AI.

## Requirement

* Last version of Arduino IDE.
* Last version of Python.
* Libraries
	* [Tkinter](http://tkinter.fdex.eu/) by Tkinter
	* [Arduino](https://www.arduino.cc/en/main/documentation) by Arduino
 

## Build Setup

Just about everything you need is setup for you.  

-   Import the project into Arduino and upload it.
-   Update values to calibrate each finger (finger1, finger2, ...) directly in the code.
-	In jankenpon.py, update the serial port your arduino, by default "COM3" is setup. /!\Don't forget it /!\
-	Make a flex sensor for each finger if the values are lower than 10 when the finger is in flex position.

Run the jankenpon.py and PLAY !

## PROJECT DOCUMENTATION

Inside the repository, you can find some files :
This SHAND folder will contain: 
- An explanation of the steps of the project : Rapport.pdf
- A graph.py, an older version to visualise in 2D the movements of the fingers in space.
- A jankenpon.py to launch the game.

The DELIVERY folder will contain:
- Some pictures on how to build a flex sensors
- Videos on how the glove work. You can visualise the detection of each fingers.

## License

This project is the property of EPITECH.
