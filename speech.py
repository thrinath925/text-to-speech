import pyttsx3
import tkinter as tk  
from tkinter  import ttk
win = tk.Tk()  
# Application Name  
win.title("Text to Speech")  
# Label  
lbl = ttk.Label(win, text = "Enter your text:").grid(column = 0, row = 0)  
# Click event  
def click(): print("Click on close")  
# Textbox widget  
name = tk.StringVar()  
nameEntered = ttk.Entry(win, width = 60, textvariable = name).grid(column = 1, row = 1)  
# Button widget  
button = ttk.Button(win, text = "submit", command = click).grid(column = 10, row = 1)  
win.mainloop()

engine = pyttsx3.init()

engine.say(name.get())

engine.runAndWait()
