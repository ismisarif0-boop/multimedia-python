# Chapter 4 (bagian 1): game Pygame sederhana dengan gambar, suara, dan animasi
import os

import pygame

BASE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE, "..", "assets")

pygame.init()

# Mengatur tampilan
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Memuat gambar dan suara
image = pygame.image.load(os.path.join(ASSETS, "example.png"))
sound = pygame.mixer.Sound(os.path.join(ASSETS, "example.wav"))

# Memutar suara saat game dimulai
sound.play()

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

pygame.quit()
