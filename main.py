import serial
from time import sleep
from tkinter import *


winRoot = Tk()
winRoot.title('LEDcontroller')
winRoot.geometry('200x200')

def isChecked():
    if rcb.get() == 1:
        dev.write(b'34')
    elif rcb.get() == 0:
        dev.write(b'2')
    # if bcb.get() == 1:
    #     dev.write(b'101')
    # elif bcb.get() == 0:
    #     dev.write(b'3')
    # if gcb.get() == 1:
    #     dev.write(b'111')
    # elif gcb.get() == 1:
    #     dev.write(b'4')



rcb = IntVar()
bcb = IntVar()
gcb = IntVar()
checkbtnRed = Checkbutton(winRoot, text="Red LED",variable=rcb,
                       onvalue=1,offvalue=0,command=isChecked)
checkbtnBlue = Checkbutton(winRoot, text="Blue LED",variable=bcb,
                       onvalue=1,offvalue=0,command=isChecked)
checkbtnGreen = Checkbutton(winRoot, text="Green LED",variable=gcb,
                       onvalue=1,offvalue=0,command=isChecked)
checkbtnRed.pack()
checkbtnBlue.pack()
checkbtnGreen.pack()
dev = serial.Serial("COM3",baudrate=19200)
print("connected")

winRoot.mainloop()
#
# class Arduino:
#     def __init__(self, port):
#         self.dev = serial.Serial(port, baudrate=19200)
#         sleep(1)
#
#     def query(self, message):
#         self.dev.write(message.encode('ascii'))
#         line = self.dev.readline()
#         return line
#
#
# board = Arduino('COM3')
# print("connected")
# i=0
# while i>5:
#     print(board.query('1'))
#     sleep(0.5)
#     print()
#     print(board.query('0'))
#     sleep(0.5)
#     i += 1
#
# print(1234)