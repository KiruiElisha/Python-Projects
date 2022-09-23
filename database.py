#!/usr/bin/env python3
import sqlite3

con = sqlite3.connect("devices")
cur = con.cursor()
cur.execute('''
        CREATE TABLE IF NOT EXISTS devices
        (SerialNo varchar(20) primary key, deviceName varchar(30), OwnerName varchar(30), RegNumber varchar(30), PhoneNumber INTEGER(20));
        ''')
cur.execute('''
        CREATE TABLE IF NOT EXISTS lost_devices
        (serialNo varchar(20) PRIMARY KEY, OwnerName varchar(30), PhoneNumber INTEGER(20));
        ''')

cur.execute('''
        CREATE TABLE IF NOT EXISTS held_devices
        (serialNo varchar(20) PRIMARY KEY, OwnerName varchar(30), PhoneNumber INTEGER(20));
        ''')
con.commit()
