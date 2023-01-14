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

listBox = tk.Listbox(canvas, fg='cyan', bg="black", width=100, font=('Sonic 1 Title Screen Outline', 10))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, text='', bg='black', fg='yellow', font=('Sonic 1 Title Screen Outline', 18))
label.pack(pady=15)

prevButton = tk.Button(canvas, text='Prev')
prevButton.pack(pady=15)

stopButton = tk.Button(canvas, text='Stop')
stopButton.pack(pady=15)


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)




canvas.mainloop()
