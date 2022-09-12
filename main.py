import tkinter as tk
import serial
from time import sleep
import random
color=["#0c1f4c","red","blue","green","yellow","black","white","brown","pink","purple"]
body =tk.Tk()
body.configure(bg="#1a0933")
seriall = serial.Serial('COM4',9800,timeout=0.05)#COM change may be needed for program to work
sleep(2)
def inputhandling():
    while True:
        coords=(seriall.readline()).decode().strip()
        a=(coords.split(","))
        if len(a)==3:       
            b=(float(a[0]),float(a[1]),float(a[2]))
            return(b)
        else:
            pass
body.geometry("600x600")    
canvas=tk.Canvas(body,width=500,height=500,bg="#6f42C1")
canvas.place(anchor="center",rely=.5,relx=.5)
circlee=canvas.create_oval(216,216,296,296,fill="#0c1f4c")
a3=1
def moveit():
    global a3
    a=inputhandling()
    print(a)
    canvas.move(circlee,((a[0])-519)/100,((a[1])-504)/100)
    if a[2]==0 and a3!=0:
        canvas.itemconfig(circlee, fill=(random.choice(color)))
    a3 =a[2]
    body.after(1,moveit)

moveit()

body.mainloop()

