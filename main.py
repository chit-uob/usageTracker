# A python project to track how long I play games, and possibly stop it

import time  # for sleep
import process_checker  # to check what processes are running
import file_manipulation  # to log things in files
import time_monitor  # to monitor how long am I playing


def print_welcome(name):
    print(f'Hi, {name}. Welcome to the usage tracker to make sure you are productive')


if __name__ == '__main__':
    print_welcome('Chit')

    was_previously_playing = False  # Because I am not playing when the script starts
    consecutive_playtime_minutes = 0

    # The main loop that runs forever
    while True:
        is_playing = process_checker.check_if_process_is_running("t2gp.exe") or process_checker.check_if_process_is_running("javaw.exe") or process_checker.check_if_process_is_running("EoCApp.exe")
        if is_playing != was_previously_playing:  # If activity changes
            if is_playing:
                time_monitor.make_ding_sound()
                file_manipulation.record_start_playing()
            else:
                file_manipulation.record_stop_playing()
                consecutive_playtime_minutes = 0  # Reset because I am not playng anymore
            was_previously_playing = is_playing  # Update

        # If on going playing
        if is_playing and was_previously_playing:
            consecutive_playtime_minutes += 1 / 6  # Because the loop runs every 10 seconds, which is 1/6 minute
            if round(consecutive_playtime_minutes, 1) % 1 == 0:  # Round time to avoid stupid float value
                time_monitor.react_to_time(round(consecutive_playtime_minutes, 1))

        time.sleep(10)  # Loop every 10 seconds
