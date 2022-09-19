#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3


con = sqlite3.connect("library")

cur = con.cursor()

def Register():
    
    serialNo = Info1.get()
    deviceName = Info2.get()
    OwnerName = Info3.get()
    RegNumber = Info4.get()
    PhoneNumber = Info5.get()
    
    insertDevice = "insert into devices values ('"+serialNo+"','"+deviceName+"','"+OwnerName+"','"+RegNumber+"','"+PhoneNumber+"')"
    try:
        cur.execute(insertDevice)
        con.commit()
        messagebox.showinfo('Success',"Device added successfully")
    except:
        messagebox.showinfo("Error","Can't add data into Database")
    
    root.destroy()

def addDevice(): 
    
        global Info1 ,Info2, Info3, Info4,Info5, Canvas1, con, cur, root
        
        root = Tk()
        root.title("Device Management System")
        root.minsize(width=400,height=400)
        root.geometry("600x500")
        con = sqlite3.connect("library")
        cur = con.cursor()
       
        Canvas1 = Canvas(root)
        
        Canvas1.config(bg="#ff6e40")
        Canvas1.pack(expand=True,fill=BOTH)
            
        headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        headingLabel = Label(headingFrame1, text="Add Devices", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        labelFrame = Frame(root,bg='black')
        labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
            
       
        lb1 = Label(labelFrame,text="Device Serial No: : ", bg='black', fg='white')
        lb1.place(relx=0.05,rely=0.2, relheight=0.08)
            
        Info1 = Entry(labelFrame)
        Info1.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.08)
            
  
        lb2 = Label(labelFrame,text=" Device Name: ", bg='black', fg='white')
        lb2.place(relx=0.05,rely=0.35, relheight=0.08)
            
        Info2 = Entry(labelFrame)
        Info2.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.08)
            
        
        lb3 = Label(labelFrame,text="Name of The Owner : ", bg='black', fg='white')
        lb3.place(relx=0.05,rely=0.50, relheight=0.08)
            
        Info3 = Entry(labelFrame)
        Info3.place(relx=0.3,rely=0.50, relwidth=0.62, relheight=0.08)
            
     
        lb4 = Label(labelFrame,text="Registration Number : ", bg='black', fg='white')
        lb4.place(relx=0.05,rely=0.65, relheight=0.08)

                
        lb3 = Label(labelFrame,text="Name of The Owner : ", bg='black', fg='white')
        lb3.place(relx=0.05,rely=0.50, relheight=0.08)
            
        Info4 = Entry(labelFrame)
        Info4.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)

        lb5 = Label(labelFrame,text="Phone Number : ", bg='black', fg='white')
        lb5.place(relx=0.05,rely=0.50, relheight=0.08)
            
        Info5 = Entry(labelFrame)
        Info5.place(relx=0.3,rely=0.65, relwidth=0.62, relheight=0.08)
            
        #Submit Button
        SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=Register)
        SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
        quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',       command=root.destroy)
        quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
        
        root.mainloop()