# Chapter 2: manipulasi gambar (Pillow) dan audio (Pydub)
import os

from PIL import Image, ImageFilter
from pydub import AudioSegment

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
os.makedirs(OUT, exist_ok=True)


def asset(name):
    return os.path.join(ASSETS, name)


def out(name):
    return os.path.join(OUT, name)


# ---------- Pillow ----------
# Memuat dan menyimpan gambar
image = Image.open(asset("example.jpg"))
image.save(out("result.jpg"))

# Cropping
cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save(out("cropped_result.jpg"))

# Resizing (dari hasil crop)
resized_image = cropped_image.resize((100, 100))
resized_image.save(out("resized_result.jpg"))

# Filtering (dari hasil resize)
filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save(out("filtered_result.jpg"))

# ---------- Pydub ----------
# Memuat dan menyimpan audio
audio = AudioSegment.from_file(asset("example.mp3"))
audio.export(out("result.mp3"), format="mp3")

# Pemotongan: 10 detik pertama
clipped_audio = audio[:10000]
clipped_audio.export(out("clipped_result.mp3"), format="mp3")

# Penggabungan
combined_audio = audio + clipped_audio
combined_audio.export(out("combined_result.mp3"), format="mp3")

# Konversi format
audio.export(out("result.wav"), format="wav")

# Pengaturan volume: naik 10 dB
louder_audio = audio + 10
louder_audio.export(out("louder_result.mp3"), format="mp3")

print("✅ Chapter 2 selesai. Hasil ada di folder output/")
