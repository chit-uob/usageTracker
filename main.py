# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import process_checker
import file_manipulation
import time_monitor


def print_welcome(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}. Welcome to the usage tracker to make sure you are productive')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_welcome('Chit')

    was_previously_playing = False
    consecutive_playtime_minutes = 0
    while True:
        is_playing = process_checker.check_if_process_is_running("t2gp.exe")
        if is_playing != was_previously_playing:
            if is_playing:
                time_monitor.make_ding_sound()
                file_manipulation.record_start_playing()
            else:
                file_manipulation.record_stop_playing()
                consecutive_playtime_minutes = 0
            was_previously_playing = is_playing
        if is_playing and was_previously_playing:
            consecutive_playtime_minutes += 1 / 6
            if (round(consecutive_playtime_minutes, 1) % 1 == 0):
                time_monitor.react_to_time(round(consecutive_playtime_minutes, 1))

        time.sleep(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
