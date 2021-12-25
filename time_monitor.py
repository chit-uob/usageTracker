# To monitor consecutive playtime
import os  # just for the next line
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # Stop pygame from displaying welcoming message
from pygame import mixer  # Need it just to play sound
import text_to_speech


def react_to_time(minutes):
    if minutes == 15:
        say_and_print("You have been playing for 15 minutes")
    if minutes == 30:
        say_and_print("You have been playing for 30 minutes")
    if minutes > 30:
        say_and_print(f"You have been playing for {minutes} minutes")


def make_ding_sound():
    mixer.init()
    mixer.music.load("audio_files/ding-sound-effect_2.mp3")
    mixer.music.play()


def say(text):
    path = text_to_speech.get_mp3_path(text)
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()


def say_and_print(text):
    print(text)
    say(text)