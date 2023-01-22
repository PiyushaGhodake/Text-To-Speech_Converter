# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from tkinter import *
import pyttsx3
from gtts import gTTS
import tkinter.font
# this module helps to
# play the converted audio
import os

# create tkinter window
root = Tk()
Msg = StringVar()
Engine = pyttsx3.init()


frame1 = Frame(root, bg="lightPink", height="150")
# for placing the widget in gui window
frame1.pack(fill=X)

frame2 = Frame(root, bg="lightPink", height="750")
frame2.pack(fill=X)

label = Label(frame1, text="TEXT TO SPEECH", font="bold, 30", bg="lightpink")
label.place(x=145, y=70)

# entry is used to enter the text
entry = Entry(frame2, textvariable=Msg, width=45, bd=4, font=14)
entry.place(x=78, y=52)
entry.insert(0, "")

def rate():
    rate = Engine.getProperty('rate')
    Engine.setProperty('rate', rate + 150)
    Engine.say(text=entry.get())
    Engine.runAndWait()


def rate1():
    rate = Engine.getProperty('rate')
    Engine.setProperty('rate', 60)
    Engine.say(text=entry.get())
    Engine.runAndWait()


def exit():
    root.destroy()


def reset():
    Msg.set("")


def play():
    # Language in which you want to convert
    language = "en"

    # Passing the text and language,
    # here we have slow=False. Which tells
    # the module that the converted audio should
    # have a high speed

    myobj = gTTS(text=entry.get(), lang=language, slow=False)

    myobj.save("convert.wav")
    os.system("convert.wav")
   # os.system() method execute the command(a string) in a subshell.



# create a button which holds
# our play function using command = play
btn = Button(frame2, text="Play", width="15", padx=7, pady=10, font="bold, 15", command=play, bg='lightblue')
btn.place(x=55, y=150)
btn1 = Button(frame2, text="Reset", width="15", padx=7, pady=10, font="bold, 15", command=reset, bg='lightblue')
btn1.place(x=245, y=150)
btn2 = Button(frame2, text="Exit", width="15", padx=7, pady=10, font="bold, 15", command=exit, bg='lightblue')
btn2.place(x=435, y=150)
btn3 = Button(frame2, text="Fast", width="15", padx=7, pady=10, font="bold, 15", command=rate, bg='lightblue')
btn3.place(x=410, y=250)
Desired_font = tkinter.font.Font(family="System", size=30, weight="bold")
label1 = Label(frame2, text="SPEED", font="bold, 15", bg="white")
label1.place(x=300, y=270)
btn4 = Button(frame2, text="Slow", width="15", padx=7, pady=10, font="bold, 15", command=rate1, bg='lightblue')
btn4.place(x=80, y=250)

Desired_font = tkinter.font.Font(family="System", size=30, weight="bold")

# Parsed the Font object
# to the Text widget using .configure( ) method.
label.configure(font=Desired_font)
# give a title
root.title("text_to_speech_convertor")
root.geometry("650x550+350+200")

# start the gui
root.mainloop()
