from time import *
from threading import Thread

def myBox():
    while True:
        print ('-----mybox is open: ')
        sleep(5)
        print ('-----My box is closed: ')
        sleep(5)

def myLed():
    while True:
        print('My LEd is on ')
        sleep(1)
        print ('My Led is off')
        sleep(1)

boxThread=Thread(target=myBox)
ledThread=Thread(target=myLed)

boxThread.daemon=True
ledThread.daemon=True

boxThread.start()
ledThread.start()

while True:
    pass