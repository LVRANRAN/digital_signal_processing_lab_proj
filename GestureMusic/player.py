import os
import pygame
import tkinter
import tkinter.filedialog
from mutagen.id3 import ID3
import random

root = tkinter.Tk()
root.minsize(300, 300)

listofsongs = []
realnames = []
v = tkinter.StringVar()
songlabel = tkinter.Label(root, textvariable=v, width=35)
index = 0

volume = 0.2


def playsong():
    global index
    index = 0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def nextsong():
    global index
    if index < len(listofsongs) - 1:
        index += 1
    else:
        index = 0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def playjay():
    global index
    index = random.randint(0, 4)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def previoussong():
    global index
    if index > 0:
        index -= 1
    else:
        index = len(listofsongs) - 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def get_cur_song():
    global index
    return str(listofsongs[index])


def stopsong():
    pygame.mixer.music.pause()
    v.set("")


def consong():
    pygame.mixer.music.unpause()
    v.set("")


def updatelabel():
    global index
    v.set(realnames[index])


def directorychooser():
    directory = tkinter.filedialog.askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith('.mp3'):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(audio['TIT2'].text[0])
            listofsongs.append(files)
            # print(files)

    pygame.mixer.init()
    # pygame.mixer.music.load(listofsongs[0])
    # pygame.mixer.music.play()


directorychooser()

label = tkinter.Label(root, text="Music Player")
label.pack()

listbox = tkinter.Listbox(root)
listbox.pack()
# List of songs
realnames.reverse()
for item in realnames:
    listbox.insert(0, item)
realnames.reverse()

'''
playbutton = tkinter.Button(root, text='Play Song')
playbutton.pack()

nextbutton = tkinter.Button(root, text='Next Song')
nextbutton.pack()

previousbutton = tkinter.Button(root, text="Previous Song")
previousbutton.pack()

stopbutton = tkinter.Button(root, text="Stop Music")
stopbutton.pack()

playbutton.bind("<Button-1>", playsong)
nextbutton.bind("<Button-1>", nextsong)
previousbutton.bind("<Button-1>", previoussong)
stopbutton.bind('<Button-1>', stopsong)
'''

songlabel.pack()

root.mainloop()
