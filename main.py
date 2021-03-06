# A python project to track how long I play games, and possibly stop it

import time  # for sleep
import process_checker  # to check what processes are running
import file_manipulation  # to log things in files
import time_monitor  # to monitor how long am I playing
import yaml

# Load config
with open('config.yaml', 'r') as f:
    yaml_config = yaml.safe_load(f)

# List of processes that are games
process_dict = {}
for process_name in yaml_config['games']:
    # Link process name to game name
    process_dict[process_name] = yaml_config['games'][process_name]


def print_welcome(name):
    print(f'Hi, {name}. Welcome to the usage tracker to make sure you are productive')


if __name__ == '__main__':

    print_welcome(yaml_config['name'])

    was_previously_playing = False  # Because I am not playing when the script starts
    consecutive_playtime_minutes = 0

    # The main loop that runs forever
    while True:
        game_list = process_checker.check_what_games_are_running(process_dict)
        is_playing = len(game_list) > 0
        if is_playing != was_previously_playing:  # If activity changes
            if is_playing:
                time_monitor.make_ding_sound()
                file_manipulation.record_start_playing(game_list[0])
            else:
                file_manipulation.record_stop_playing()
                consecutive_playtime_minutes = 0  # Reset because I am not playing anymore
            was_previously_playing = is_playing  # Update

        # If on going playing
        if is_playing and was_previously_playing:
            consecutive_playtime_minutes += 1 / 6  # Because the loop runs every 10 seconds, which is 1/6 minute
            if round(consecutive_playtime_minutes, 1) % 1 == 0:  # Round time to avoid stupid float value
                time_monitor.react_to_time(round(consecutive_playtime_minutes, 1))

        time.sleep(10)  # Loop every 10 seconds
