import pygame
pygame.init()

pygame.mixer.music.load('trilha.mp3')
pygame.mixer.music.play()
pygame.event.wait()