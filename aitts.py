# MozillaTTS_Wrapper by perseus.
# Sorry for the million comments, just wanted to make this as beginner friendly as possible.
from os import system # Importing system to use the cmd
import pygame # Importing pygame to play the wav file outputted by the tts

volume = 0.5 # Change this depend on your liking.

pygame.init() # Initializing Pygame


def speak(string):
    print("tts --text " + '"' + string + '"') # Here, this will get printed so that you know if your input will be catched.
    system("tts --text " + '"' + string + '"') # Command will be passed through system
    soundObj = pygame.mixer.Sound('tts_output.wav') # Output wav will be played by this line.
    soundObj.set_volume(volume) # Default volume will be set here.

    while True: # Loop
        if not pygame.mixer.get_busy(): # If pygame is not playing any file, this will get executed
            soundObj.play() # Playing file
            break # Breaking the loop after playing the file.



