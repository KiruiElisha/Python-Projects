#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("devices")
cur = con.cursor()

def search():
    
    global searchBtn,labelFrame,lb1,inf1,quitBtn,root,Canvas1
    
    serialNo = inf1.get()

    
    
    extractdevice = "SELECT * FROM devices WHERE serialNo = "+serialNo
    try:
        cur.execute(extractdevice)
        con.commit()
        messagebox.showinfo('Success', "Device Found!")
    except:
        messagebox.showerror('Not Found',"Details of The device not found")     


def SearchDevice(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Device Management System")
    root.minsize(width=400,height=400)
    root.geometry("600x500")
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#D6ED17")
    Canvas1.pack(expand=True,fill=BOTH)
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Search For a Device", bg='black', fg='white', font=('Courier',15))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    lb1 = Label(labelFrame,text="SerialNo : ", bg='black', fg='white')
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    

    
    
    #Issue Button
    searchBtn = Button(root,text="Search",bg='#d1ccc0', fg='black',command=search)
    searchBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()