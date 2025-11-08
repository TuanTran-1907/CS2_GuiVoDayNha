import pygame

pygame.mixer.init()

theme  = pygame.mixer.music
theme.load("thayDunghat.mp3")
pygame.mixer.music.set_volume(0.7)

btn = pygame.mixer.Sound("bubble.mp3")
btn.set_volume(0.9)

led = pygame.mixer.Sound("switch.mp3")
led.set_volume(0.9)

def play_music():
    if not pygame.mixer.music.get_busy():
        theme.play(-1)

def stop_music():
    pygame.mixer.music.stop()

def btn_sound():
    btn.play()

def led_sound():
    led.play()
