# Faça um programa que abra e reproduza um áudio de arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('A mesa.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
