#!/usr/bin/env python3

from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

con = sqlite3.connect("devices")
cur = con.cursor()

def deleteDevice():
    
    serialNo = Info1.get()
    
    deleteSql = "delete from devices where serialNo = '"+serialNo+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        messagebox.showinfo('Success',"Device Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check The serial Number")
    
    print(serialNo)
    Info1.delete(0, END)
    root.destroy()


def delete(): 
    
        global Info1,Canvas1,con,cur,root
        
        root = Tk()
        root.title("Device Management System")
        root.minsize(width=400,height=400)
        root.geometry("600x500")
        Canvas1 = Canvas(root)
        Canvas1.config(bg="#006B38")
        Canvas1.pack(expand=True,fill=BOTH)
            
        headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
        headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
            
        headingLabel = Label(headingFrame1, text="Delete a Device", bg='black', fg='white', font=('Courier',15))
        headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
        
        labelFrame = Frame(root,bg='black')
        labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
            
        lb2 = Label(labelFrame,text="Device Serial Number : ", bg='black', fg='white')
        lb2.place(relx=0.05,rely=0.5)
            
        Info1 = Entry(labelFrame)
        Info1.place(relx=0.3,rely=0.5, relwidth=0.62)
        
        #Submit Button
        SubmitBtn = Button(root,text="DELETE",bg='#f50511', fg='black',command=deleteDevice)
        SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
        
        quitBtn = Button(root,text="Quit",bg='#0511f5', fg='black', command=root.destroy)
        quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
        
        root.mainloop()