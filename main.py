import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title('Music Player')
canvas.geometry('600x800')
canvas.config(bg='black')

rootpath = "C:\\Users\\Константин\\Desktop\\music"
pattern = "*.mp3"

mixer.init()

prev_img = tk.PhotoImage(file="prev.png")
next_img = tk.PhotoImage(file="next.png")
pause_img = tk.PhotoImage(file="pause.png")
play_img = tk.PhotoImage(file="play.png")
stop_img = tk.PhotoImage(file="stop.png")


def select():
    label.config(text=listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


def pause_song():
    if pauseButton['text'] == 'Pause':
        mixer.music.pause()
        pauseButton['text'] = 'Play'
    else:
        mixer.music.unpause()
        pauseButton['text'] = 'Pause'


def quarter_volume():
    mixer.music.set_volume(0.25)


def half_volume():
    mixer.music.set_volume(0.5)


def third_volume():
    mixer.music.set_volume(0.75)


def all_volume():
    mixer.music.set_volume(0.1)


listBox = tk.Listbox(canvas, fg='cyan', bg="black", width=100, font=('Sonic 1 Title Screen Outline', 10))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('Sonic 1 Title Screen Outline', 18))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=5, anchor='center')

prevButton = tk.Button(canvas, text='Prev', image=prev_img, bg='black', borderwidth=0, command=play_prev)
prevButton.pack(pady=15, in_=top, side='left')

stopButton = tk.Button(canvas, text='Stop', image=stop_img, bg='black', borderwidth=0, command=stop)
stopButton.pack(pady=15, in_=top, side='left')

playButton = tk.Button(canvas, text='Play', image=play_img, bg='black', borderwidth=0, command=select)
playButton.pack(pady=15, in_=top, side='left')

pauseButton = tk.Button(canvas, text='Pause', image=pause_img, bg='black', borderwidth=0, command=pause_song)
pauseButton.pack(pady=15, in_=top, side='left')

nextButton = tk.Button(canvas, text='Next', image=next_img, bg='black', borderwidth=0, command=play_next)
nextButton.pack(pady=15, in_=top, side='left')

quartVolumeButton = tk.Button(canvas, text='25', bg='white', borderwidth=0, command=quarter_volume)
quartVolumeButton.pack(pady=15, in_=top, side='left')

halfVolumeButton = tk.Button(canvas, text='50', bg='white', borderwidth=0, command=half_volume)
halfVolumeButton.pack(pady=15, in_=top, side='left')

thirdVolumeButton = tk.Button(canvas, text='75', bg='white', borderwidth=0, command=third_volume)
thirdVolumeButton.pack(pady=15, in_=top, side='left')

allVolumeButton = tk.Button(canvas, text='100', bg='white', borderwidth=0, command=third_volume)
allVolumeButton.pack(pady=15, in_=top, side='left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
