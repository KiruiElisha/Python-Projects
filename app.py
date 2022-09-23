#!/usr/bin/env python3

import py_compile
import sqlite3
from tkinter import *
from tkinter.ttk import *
import PIL
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from AddDevice import addDevice
from Search import SearchDevice, search
from Report import *
from ViewDevice import View
from DeleteDevice import delete


root = Tk()
root.title = "Device Management System"
root.minsize(width=400,height=400)
root.geometry("1000x500")

same=True
n=0.25
# Adding a background image
background_image =Image.open("devices.jpeg")
[imageSizeWidth, imageSizeHeight] = background_image.size
newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 
    
background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = Canvas(root)
Canvas1.create_image(600,500,image = img)      
Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)


headingFrame1 = Frame(root,bg="#000108",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.2)
headingLabel = Label(headingFrame1, text="MULTIMEDIA UNIVERSITY OF KENYA \n --------------------------------\n DEVICE MANAGEMENT SYSTEM", bg='blue', fg='black', font=('Courier',20))
headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text= 'Add a Device', bg='black', fg='White', command=addDevice)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)

btn2 = Button(root, text= 'Remove a device', bg='black', fg='White', command=delete)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)

btn3 = Button(root, text= 'View Devices', bg='black', fg='White', command=View)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

btn4 = Button(root, text= 'Search For a Device', bg='black', fg='White', command=search)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

btn5 = Button(root, text= 'Report A Lost Device', bg='black', fg='White', command=addDevice)
btn5.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)

root.mainloop()