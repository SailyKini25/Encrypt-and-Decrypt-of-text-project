from tkinter import *

def show_entry_field():
     print("PROJECT BY SAILY KINI")
     print("Enter your massage:%s\n Your  encrypted message is:%s\n Enter your encrypt message for decryption:%s\n Your decrypted message is:%s\n"%(e1.get(),e2.get(),e3.get(),e4.get()))

     def __init__(self, master):
         self.master = master

master=Tk()
Label(master,text="Enter your message:").grid(row=0)
Label(master,text="Your encrypted message is:").grid(row=4)
Label(master,text="Enter your encrypt message for decrypt:").grid(row=6)
Label(master,text="Your decrypted message is:").grid(row=8)

alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 4

var1 = StringVar()
var2 = StringVar()
var3 = StringVar()
var4 = StringVar()



e1=Entry(textvariable=var1)
e2=Entry(textvariable=var2)
e3=Entry(textvariable=var3)
e4=Entry(textvariable=var4)

e1.grid(row=0,column=2)
e2.grid(row=4,column=2)
e3.grid(row=6,column=2)
e4.grid(row=8,column=2)



def encrypt():
        newmessage = ''
        mystring = var1.get()
        for character in mystring:
               if character in alphabet:
                 position = alphabet.find(character)
                 newposition = (position + int(key)) % 26
                 newcharacter = alphabet[newposition]
                 newmessage += newcharacter
               else:
                newmessage += character
        var2.set(newmessage)
        return


def decrypt():
        newmessage = ''
        mystring = var3.get()
        for character in mystring:
            if character in alphabet:
                position = alphabet.find(character)
                newposition = (position - int(key)) % 26
                newcharacter = alphabet[newposition]
                newmessage += newcharacter
            else:
                newmessage += character
        var4.set(newmessage)

        return

b1=Button(master,text="Encrypt",command=encrypt).grid(row=2,column=2)
b2=Button(master,text="Decrypt",command=decrypt).grid(row=7,column=2)
Button(master,text="Close",command=master.quit).grid(row=10,column=2)



mainloop()
