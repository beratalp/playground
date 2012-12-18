#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkMessageBox import*
import subprocess

try:

    def buttonOlay():
        getmessage()
        sendmessage(message, baslik)

    def getmessage():
        message = messageInput.get()
        baslik = baslikInput.get()
        global message
        global baslik

    def sendmessage(message, baslik):
        subprocess.Popen(['notify-send',baslik, message])
        return

    pencere = Tk()
    pencere.title("D-Bus Mesaj Gönderici")
    pencere.geometry("300x300")
    label = Label(text="Notify-OSD ile mesaj gönderebilirsiniz. \n İlk satıra başlığı, ikinci satıra ise mesajı yazın")
    label.pack()
    baslikInput=Entry()
    baslikInput.pack()
    messageInput=Entry()
    messageInput.pack()
    button = Button(text="Gönder",command=buttonOlay)
    button.pack()
    mainloop()
except :
    showerror("Hata","Hata")
