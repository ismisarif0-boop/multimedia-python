"""Membuat file media contoh (example.*) di folder assets/ untuk keperluan tutorial."""
import os

import numpy as np
from moviepy.editor import ImageSequenceClip
from PIL import Image, ImageDraw
from pydub import AudioSegment
from pydub.generators import Sine

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(ASSETS, exist_ok=True)


def path(name):
    return os.path.join(ASSETS, name)


# example.jpg: gradien warna dengan beberapa bentuk
w, h = 640, 480
x, y = np.meshgrid(np.arange(w), np.arange(h))
gradient = np.dstack([x * 255 // w, y * 255 // h, np.full((h, w), 160)]).astype("uint8")
img = Image.fromarray(gradient)
draw = ImageDraw.Draw(img)
draw.ellipse((150, 100, 350, 300), fill=(255, 220, 0), outline="white", width=4)
draw.rectangle((300, 250, 560, 420), fill=(30, 30, 30), outline="white", width=4)
draw.text((20, 20), "example image", fill="white")
img.save(path("example.jpg"))

# example.png: sprite kecil transparan untuk Pygame
sprite = Image.new("RGBA", (64, 64), (0, 0, 0, 0))
ImageDraw.Draw(sprite).ellipse((4, 4, 60, 60), fill=(220, 40, 40, 255), outline="white", width=3)
sprite.save(path("example.png"))

# example.mp3 (20 detik, nada naik) dan example.wav (beep pendek)
melody = sum(
    (Sine(f).to_audio_segment(duration=500).fade_in(20).fade_out(20) for f in [262, 294, 330, 349, 392, 440, 494, 523] * 5),
    AudioSegment.empty(),
)
melody.export(path("example.mp3"), format="mp3")
Sine(880).to_audio_segment(duration=300).fade_out(100).export(path("example.wav"), format="wav")

# example.mp4: 12 detik, 24 fps, kotak bergerak
fps, seconds = 24, 12
frames = []
for i in range(fps * seconds):
    frame = np.zeros((240, 320, 3), dtype="uint8")
    frame[:] = (i * 255 // (fps * seconds), 60, 120)
    px = (i * 4) % 280
    frame[100:140, px : px + 40] = (255, 255, 255)
    frames.append(frame)
ImageSequenceClip(frames, fps=fps).write_videofile(path("example.mp4"), codec="libx264", logger=None)

print("Aset dibuat di", ASSETS)
