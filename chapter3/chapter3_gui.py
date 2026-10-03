# Chapter 3 (bagian 2): GUI Tkinter dengan integrasi gambar dan audio
import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk
from pydub import AudioSegment
from pydub.playback import play

BASE = os.path.dirname(os.path.abspath(__file__))

# Membuat jendela utama
root = tk.Tk()
root.title("Multimedia Application")

# Menampilkan gambar (Pillow -> format Tkinter)
image = Image.open(os.path.join(BASE, "..", "assets", "example.jpg"))
photo = ImageTk.PhotoImage(image)

label = tk.Label(root, image=photo)
label.pack()


# Fungsi untuk memutar musik
def play_music():
    file_path = filedialog.askopenfilename()
    if file_path:
        audio = AudioSegment.from_file(file_path)
        play(audio)


# Tombol untuk memutar musik
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack()

# Menjalankan loop acara Tkinter
root.mainloop()
