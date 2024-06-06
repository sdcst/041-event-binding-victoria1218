import tkinter as tk 
from tkinter import *
from tkinter import ttk
import playsound as p

def Banana(event):
    print(event)
    p.playsound("bigbanana.mp3")

def Dogbark(event):
    print(event) 
    p.playsound("animals_dogs_x2_barking_small_001.mp3")

def Clock(event):
    print(event)
    p.playsound("clock.mp3") 

def Alarm(event):
    print(event)
    p.playsound("alarmsound.mp3") 

def Raining(event):
    print(event)
    p.playsound("raining.mp3")

def Bird(event):
    print(event)
    p.playsound("birdsound.mp3")

win = tk.Tk()
win.title()
win.attributes("-topmost",True)

banana = PhotoImage(file = "banana.png",width=250, height=250)
clock = PhotoImage(file= "clock.png", width=250, height=250)
dogbark = PhotoImage(file= "dogdog.png", width=250,height=250)
alarm = PhotoImage(file= "alarm.png", width=250, height=250)
raining = PhotoImage(file = "raining.png", width=250,height=250)
bird = PhotoImage(file = "bird.png",width=250, height=250)

l1 = tk.Label(win,text="Press any button to play a sound")
l2 = tk.Button(win, text="Banana", relief=GROOVE, image= banana)
l2.bind("<Button>",Banana)
l3 = tk.Button(win, text="Clock Alarm",relief=GROOVE, image=clock)
l3.bind("<Button>", Clock)
l4 = tk.Button(win, text="Dogdogdog",relief=GROOVE, image=dogbark)
l4.bind("<Button>", Dogbark)
l5 = tk.Button(win, text="Alarm",relief=GROOVE, image=alarm)
l5.bind("<Button>", Alarm)
l6 = tk.Button(win, text="Raining",relief=GROOVE, image=raining)
l6.bind("<Button>", Raining)
l7 = tk.Button(win, text="Bird",relief=GROOVE, image=bird)
l7.bind("<Button>", Bird)




l1.grid(row=1, column=2)
l2.grid(row=2, column=1)
l3.grid(row=2, column=2)
l4.grid(row=2, column=3)
l5.grid(row=3, column=1)
l6.grid(row=3, column=2)
l7.grid(row=3, column=3)



win.mainloop()