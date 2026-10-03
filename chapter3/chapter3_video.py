# Chapter 3 (bagian 1): manipulasi video dengan MoviePy
import os

from moviepy.editor import VideoFileClip, concatenate_videoclips, vfx

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "output")
os.makedirs(OUT, exist_ok=True)


def out(name):
    return os.path.join(OUT, name)


# Memuat dan menyimpan video
video = VideoFileClip(os.path.join(BASE, "..", "assets", "example.mp4"))
video.write_videofile(out("result.mp4"))

# Pemotongan: 10 detik pertama
short_video = video.subclip(0, 10)
short_video.write_videofile(out("short_result.mp4"))

# Penggabungan
combined_video = concatenate_videoclips([video, short_video])
combined_video.write_videofile(out("combined_result.mp4"))

# Efek: pembalikan waktu
reversed_video = short_video.fx(vfx.time_mirror)
reversed_video.write_videofile(out("reversed_result.mp4"))

# Kecepatan: 2x lebih cepat
sped_up_video = short_video.fx(vfx.speedx, 2)
sped_up_video.write_videofile(out("sped_up_result.mp4"))

print("✅ Chapter 3 (video) selesai. Hasil ada di folder output/")
