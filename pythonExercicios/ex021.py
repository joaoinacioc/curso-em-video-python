# Faça um programa em Python que abra e reproduza o áudio de
# um arquivo MP3.
import time

from pygame import mixer

mixer.init()
mixer.music.load('C:/Users/joaov/Downloads/jarvis.mp3')
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)
