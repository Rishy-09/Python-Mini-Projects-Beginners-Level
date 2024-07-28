# from playsound import playsound
import pygame
import time

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")

    pygame.mixer.init()
    pygame.mixer.music.load("AK-47-firing.mp3")
    pygame.mixer.music.play()

    # wait until the sound finishes
    while pygame.mixer.music.get_busy():
        time.sleep(1)

    # playsound("AK-47-firing.mp3")

minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)

# playsound is not working so using pygame instead

# pygame.mixer.music.get_busy() // Purpose: 
# This method checks if any music is currently playing. 
# It returns True if the mixer is busy playing a sound, and False otherwise.

# for supressing the into message of pygame module we can re-direct the message to some file that dissolves on its own