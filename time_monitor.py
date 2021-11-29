# To monitor consecutive playtime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

def react_to_time(minutes):
    if minutes == 30:
        print("You have been playing for 30 minutes!")
        make_ding_sound()
    if minutes == 45:
        print("You have been playing for 45 minutes")
        make_ding_sound()
    if minutes > 45:
        print(f"You have been playing for {minutes} minutes")
        make_ding_sound()



def make_ding_sound():
    mixer.init()
    mixer.music.load("audio_files/ding-sound-effect_2.mp3")
    mixer.music.play()