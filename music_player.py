import pyttsx3
import os
import keyboard
from mutagen.mp3 import MP3
from pygame import mixer
from datetime import datetime
from tkinter.constants import LEFT, RIGHT
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import *
from tkinter import filedialog
import shutil

def play_welcome_msg():
    engine = pyttsx3.init()
    engine.say('Good morning, Namaste, Welcome you all!')
    engine.runAndWait()

def readable_date_info(date):
    return date.ctime()

def add_music():
    x = [dirs for dirs in os.listdir(os.getcwd())]
    if 'songs' not in x:
        os.makedirs('songs')

    filenames = filedialog.askopenfilenames(initialdir = os.getcwd(),
        title = "Select files",
        filetypes = (("Audio files",
                    "*.mp3*"),
                    ("all files","*.*"))
        )

    try:
        for filename in filenames:
            shutil.copy(filename, os.path.join(os.getcwd(), 'songs'))    
    except OSError:
        pass  

def quit_player():
    r.destroy()
    return

def play_songs():
    songs = []
    try:
        songs_folder = os.path.join(os.getcwd(), 'songs')
        for files in os.listdir(songs_folder):
            if files.endswith('.mp3'):
                songs.append(files)
    except OSError:
        pass    
    finally:
        for song in songs:
            mixer.init()
            song_path = os.path.join(os.getcwd()+'//songs', song)
            mixer.music.load(song_path)
            mixer.music.play()
            
            while mixer.music.get_busy():
                if keyboard.is_pressed('p'):
                    mixer.music.pause()
                    state = 'paused'
                    while state == 'paused':
                        if keyboard.is_pressed('q'):
                            quit_player()
                        if keyboard.is_pressed('r'):
                            mixer.music.unpause()
                            state = 'playing'
                
                elif keyboard.is_pressed('q'):
                    quit_player()

                else:
                    continue                

r = tk.Tk()
r.iconbitmap('icon.ico')
height= r.winfo_screenheight()
r.geometry("1100x%d" % (height))
r.title('IK TechServe')
r.configure(background='black')

play_welcome_msg()

today_date = readable_date_info(datetime.now())
today_panel = Label(r, text = today_date, font =('Jokerman', 35), foreground='hotpink', background='black')
today_panel.grid(column=0, row=0, columnspan=3, padx='50px', pady='20px')

music_add = tk.Button(r, text="Add Music", fg='yellow', bg='black', font=('Jokerman', 30), command=add_music)
music_add.grid(column=3, row=0, columnspan=2, padx='10px', pady='10px')

file = Image.open('bg-final.png')

pixels_x, pixels_y = int(0.6*file.size[0]), int(0.5*file.size[1]) 
img = ImageTk.PhotoImage(file.resize((pixels_x, pixels_y)))
panel = Label(r, image = img, borderwidth=0, relief='flat')
panel.grid(column=0, row=1, columnspan=5, padx='30px', pady='30px')

music_serve = tk.Button(r, text="Play d MuSIc", fg='yellow', bg='black', font=('Jokerman', 30), command=play_songs)
music_serve.grid(column=2, row=2, columnspan=2)

r.mainloop()