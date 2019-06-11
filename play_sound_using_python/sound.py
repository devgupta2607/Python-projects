import pygame.mixer
from time import sleep

pygame.mixer.init()
pygame.mixer.music.load(open("D:\hello.wav","rb"))

pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    sleep(5)

print ("done")
