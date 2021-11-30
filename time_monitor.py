# To monitor consecutive playtime
import os  # just for the next line
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Stop pygame from displaying welcoming message
from pygame import mixer  # Need it just to play sound


def react_to_time(minutes):
    if minutes == 15:
        print("You have been playing for 15 minutes!")
        make_ding_sound()
    if minutes == 30:
        print("You have been playing for 30 minutes")
        make_ding_sound()
    if minutes > 30:
        print(f"You have been playing for {minutes} minutes")
        make_ding_sound()


def make_ding_sound():
    mixer.init()
    mixer.music.load("audio_files/ding-sound-effect_2.mp3")
    mixer.music.play()
