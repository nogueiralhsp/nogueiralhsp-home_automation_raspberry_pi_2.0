# from tkinter.constants import S
import requests
import json

import tkinter as tk
from tkinter import *

import time


from models.devices import *
from utils.internet_connection_check import *
from config.global_vars import *


apiRefreshTime = 2000  # time to call api for refreshing / call api

deviceList = ["GarageFrame","12341234","Garage","Workbench Light",'bool']

# # //Creating Device Model
device1 = Device("GarageFrame","12341234","Garage","Workbench Light",'bool')

# function that run all the functions to be ran at the start
def functionUpdates():
    print('running updates')
    if internetConnectionCheck() == True:
        # here call function for when it is online
        onlineStatus.config(background='green', text='We are on-line')

    else:
        onlineStatus.config(background='red', text='We are off-line')
    
    # runs update after apiRefreshTime
    root.after(apiRefreshTime, functionUpdates)
    


def exit_app():
    root.destroy()

# ***************************************************************************
#                        here starts creating window                        *
# ***************************************************************************


# vars used on GUI
lableWidth = 15
lableHeigh = 1
buttonWidth = 15
buttonHeight = 1


# Create Window
root = tk.Tk()
root.geometry('400x480')

mainContainerFrame = Frame(
    root
)
mainContainerFrame.pack(
    fill='both',
    side='top',
    expand='yes'
)
# ***************    # Frames # ***************     

mainContainerFrame.pack(
    fill='both',
    side='top',
    expand='yes'
)

# Status Components
onlineStatus = Label(
    mainContainerFrame,
    text='Loading...',
    width=lableWidth,
    height=lableHeigh,
)
onlineStatus.pack()

# temperature entry
temperatureEntry = Entry(
    mainContainerFrame,
    width=15
)
temperatureEntry.insert(0, 'loading...')
temperatureEntry.pack()

# close window/application button
closeButton = Button(
    root,
    text='Close',
    width=buttonWidth,
    height=buttonHeight,
    command=exit_app
)
closeButton.pack(side='bottom')

for x in deviceList:
    x = Label(
        mainContainerFrame,
        text=x,
        width=lableWidth,
        height=lableHeigh,
    )
    x.pack()


root.after(apiRefreshTime, functionUpdates)

# main loop root
root.mainloop()