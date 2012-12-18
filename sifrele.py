#-*-coding:utf-8-*-
from tkMessageBox import *
from Tkinter import *
import sys
class App:
    def __init__(self):
        try:
            self.root=Tk()
            self.root.geometry("400x250+500+300")
            self.root.config(bg="black")
            self.root.resizable(width=FALSE, height=FALSE)
            self.root.title("Şifrele")
            self.ana_menu=Menu(self.root,fg="black")
            self.root.config(menu=self.ana_menu,bg="black")
            self.mode=Menu(self.ana_menu,tearoff=0,font=("Ariel",10,"bold"),bg="black",fg="green")
            self.ana_menu.add_cascade(label="Menü",menu=self.mode)
            self.mode.add_command(label="md5",font=("Ariel",10,"bold"),command=self.md5_PenAr)
            self.mode.add_command(label="base64",font=("Ariel",10,"bold"),command=self.base64_PenAr)
            self.mode.add_command(label="sha",font=("Ariel",10,"bold"),command=self.sha_PenAr)
            self.mode.add_command(label="sha224",font=("Ariel",10,"bold"),command=self.sha224_PenAr)
            self.mode.add_command(label="sha256",font=("Ariel",10,"bold"),command=self.sha256_PenAr)
            self.mode.add_command(label="sha384",font=("Ariel",10,"bold"),command=self.sha384_PenAr)
            self.mode.add_command(label="sha512",font=("Ariel",10,"bold"),command=self.sha512_PenAr)
            self.mode.add_command(label="Çıkış",font=("Helvetica",9,"bold"),command=sys.exit)
            self.help=Menu(self.ana_menu,tearoff=0,font=("Ariel",10,"bold"),bg="black",fg="green")
            self.ana_menu.add_cascade(label="Yardım",menu=self.help)
            self.help.add_command(label="Yardım",font=("Ariel",10,"bold"),command=self.menu_help)
            self.base64_PenAr()
            self.root.mainloop()
        except:
            pass
    def base64_Crypt(self):
        import base64
        self.hash=base64.encodestring(self.giris.get())
        self.metin.insert(END,self.hash)
            
    def base64_Decrypt(self):
        import base64
        self.hash=base64.decodestring(self.giris.get())
        self.metin.insert(END,self.hash)
        
    def md5_Crypt(self,event):
        import md5
        self.hash=md5.new()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def sha_Crypt(self,event):
        import sha
        self.hash=sha.new()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def sha224_Crypt(self,event):
        import hashlib
        self.hash=hashlib.sha224()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def sha256_Crypt(self,event):
        import hashlib
        self.hash=hashlib.sha256()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def sha384_Crypt(self,event):
        import hashlib
        self.hash=hashlib.sha384()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def sha512_Crypt(self):
        import hashlib
        self.hash=hashlib.sha512()
        self.hash.update(self.giris.get())
        self.metin.insert(END,self.hash.hexdigest())

    def md5_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.md5_Crypt)

    def base64_PenAr(self):
        self.label1=Label(text="Giriş",bg="black",fg="green").place(x=45,y=3)
        self.giris=Entry()
        self.giris.config(bg="green")
        self.giris.place(width="300",x=50,y=20)
        self.label2=Label(text="Çıkış",bg="black",fg="green").place(x=45,y=45)
        self.metin=Text(font="Helvetica 13 bold")
        self.metin.config(bg="green")
        self.metin.place(height="100",width="300",x=50,y=65)
        self.b1=Button(text="Şifrele",bg="black",fg="green",borderwidth="3")
        self.b1.config(relief=RAISED,command=self.base64_Crypt)
        self.b1.place(x=50,y=200)
        self.b2=Button(text="Çöz",bg="black",fg="green",borderwidth="3")
        self.b2.config(relief=RAISED,command=self.base64_Decrypt)
        self.b2.place(x=200,y=200)

    def sha_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.sha_Crypt)

    def sha224_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.sha224_Crypt)

    def sha256_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.sha256_Crypt)

    def sha384_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.sha384_Crypt)

    def sha512_PenAr(self):
        self.Pen_Ar()
        self.root.bind("<Return>",self.sha512_Crypt)

    def sil(self):
        self.giris.destroy()
        self.metin.destroy()
        self.b1.destroy()
        self.b2.destroy()

    def menu_help(self):
        self.pencere=Toplevel()
        self.pencere.title("Help")
        self.pencere.geometry("430x110+400+200")
        #self.pencere.resizable(width=FALSE, height=FALSE)
        self.L=Label(self.pencere,text="Program base64 modunda calisir.Diger sifreleme algoritmalarini \n kullanmak icin 'menu' u kullaniniz.\nBase64 modundayken 'input'a girilen veriyi sifrelemek icin 'encode',\nsifrelenmis veriyi eski haline getirmek icin \nsifreli veriyi 'input'a yapistirdiktan sonra 'decode' dugmesini kullaniniz.\nBase64 haricindeki sifreleme algoritmalari geri donusumsuzdur \nve kullanmak icin 'enter' tusuna basmaniz yeterli olacaktir.",bg="black",fg="green").place(x=1,y=1)

    def Pen_Ar(self):
        self.sil()
        self.label1=Label(text="Input",bg="black",fg="green").place(x=45,y=3)
        self.giris=Entry()
        self.giris.config(bg="green")
        self.giris.place(width="300",x=50,y=20)
        self.label2=Label(text="Output",bg="black",fg="green").place(x=45,y=45)
        self.metin=Text(font="Helvetica 13 bold")
        self.metin.config(bg="green")
        self.metin.place(height="100",width="300",x=50,y=65)

root=App()