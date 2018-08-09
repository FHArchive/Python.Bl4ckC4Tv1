# Bl4ckC4T v1 with tkinter gui
import tkinter
from tkinter import *

def start():
    keystring = ''.join(fieldkey.get(1.0, END).split())
    choice = var1.get()

    outstring = ""
    inputstring = fieldinp.get(1.0, END)
    for index in range(len(inputstring)-1):
        if index >= len(keystring):
            keystring += keystring
        if choice == 1:
            charint = ord(inputstring[index]) + ord(keystring[index]) - 1
        else:
            charint = ord(inputstring[index]) - ord(keystring[index]) + 1
        outstring += chr(charint)
    updateoutput(outstring)

def updateoutput(outstring):
    fieldout.delete(1.0, END)
    fieldout.insert(1.0, outstring)


win = tkinter.Tk()
win.minsize(400,650)
win.wm_title("Bl4ckC4T v1")

try:
    win.tk.call('wm', 'iconphoto', win._w, tkinter.PhotoImage(file='blackcat.png'))
except:
    pass

offsetl = 35
offsett = 40

# title
lblkey = Label(text = "Bl4ckC4T version 1 with tkinter ", font = 80)
lblkey.place(x = offsetl + 0,y = 10)

# key
lblkey = Label(text = "Key:")
lblkey.place(x = offsetl + 0,y = offsett + 0)
fieldkey = Text(height = 4, width = 40)
fieldkey.place(x = offsetl + 0,y = offsett + 25)

# input
lblinp = Label(text = "Input:")
lblinp.place(x = offsetl + 0,y = offsett + 100)
fieldinp = Text(height = 10, width = 40)
fieldinp.place(x = offsetl + 0,y = offsett + 125)

# encrypt decrypt buttons
lblsel = Label(text = "Select a mode:")
lblsel.place(x = offsetl + 0,y = offsett + 300)
var1 = IntVar()
radioncr = Radiobutton(text = "Encrypt", variable = var1,  value = 1,)
radioncr.place(x = offsetl + 0,y = offsett + 325)
radiodcr = Radiobutton(text = "Decode", variable = var1,  value = 2,)
radiodcr.place(x = offsetl + 0,y = offsett + 350)
radioncr.select()

# DO IT
btnrun = tkinter.Button(text = "--- Run ---", command = start)
btnrun.place(x = offsetl + 130,y = offsett + 370)

# output
lblout = Label(text = "Output:")
lblout.place(x = offsetl + 0,y = offsett + 400)
fieldout = Text(width = 40, height = 10)
fieldout.place(x = offsetl + 0,y = offsett + 425)

win.mainloop()

