import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
import ftplib
import os
import time
import ntpath 

from tkinter import filedialog
from pathlib import Path


from playsound import playsound
import pygame
from pygame import mixer

window=Tk()
window.title('Music Window')
window.geometry("300x300")
window.configure(bg="LightSkyBlue")

PORT = 8050
IP_ADDRESS = '127.0.0.2'
SERVER = None
BUFFER_SIZE = 4096

song_counter = 0
song_selected = None

infoLabel = None
listbox = None

def pause():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.pause()

def resume():
    global song_selected

    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.play()

def stop():
    global song_selected

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.pause()
    infoLabel.configure(text="")

def play():
    global song_selected
    song_selected = listbox.get(ANCHOR)

    pygame
    mixer.init()
    mixer.music.load("shared_files/"+song_selected)
    mixer.music.play()
    if(song_selected != ""):
        infoLabel.configure(text="Now Playing: "+song_selected)
    else:
        infoLabel.configure(text="")

def musicWindow():
    selectlabel = Label(window, text="Select Song",bg="cyan",font=("Calibri",8))
    selectlabel.place(x=2, y=1)

    listbox = Listbox(window,height=10,weight=39,activestyle="dotbox",bg="cyan",borderwidth=2, font=("Calibri",10))
    listbox.place(x=10,y=10)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    PlayButton = Button(window,text="Play",width=10,bd=1,bg="Blue",font=("Calibri",10),command=play)
    PlayButton.place(x=30,y=200)

    Stop = Button(window,text="Stop",bd=1,width=10,bg="Blue",font=("Calibri",10),command=stop)
    Stop.place(x=200,y=200)

    Upload = Button(window,text="Upload",width=10,bd=1,bg="Blue",font=("Calibri",10))
    Upload.place(x=30,y=250)

    Download = Button(window,text="Download",width=10,bd=1,bg="Blue",font=("Calibri",10))
    Download.place(x=200,y=250)

    infoLabel = Label(window,text="",fg="Blue",font=("Calibri",10))
    infoLabel.place(x=4,y=280)

    ResumeButton = Button(window,text="Resume",width=10,bd=1,bg="cyan",font=("Calibri",10),command=resume)
    ResumeButton.place(x=30,y=250)

    PauseButton = Button(window,text="Pause",width=10,bd=1,bg="cyan",font=("Calibri",10),command=pause)
    PauseButton.place(x=200,y=250)

    for file in os.listdir("shared_files"):
        filename = os.fsdecode(file)
        listbox.insert(song_counter,filename)
        song_counter = song_counter + 1

    window.mainloop()
 
def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS,PORT))

    musicWindow()

setup()
