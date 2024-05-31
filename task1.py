import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")


win= tk.Tk

b1 = tk.Button(win,text="Click to play")
b1.bind("<Buttom>",playsound)

b1.pack

win.mainloop()