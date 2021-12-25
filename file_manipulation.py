# To save/get data from file
import pathlib  # for better path handling
from datetime import datetime  # To record accurate time


VERSION_CODE = ".v1"


pathlib.Path(r"data_files/").mkdir(parents=True, exist_ok=True)


def get_file_path():
    date_format = datetime.now().strftime("%Y%m%d")
    filepath = pathlib.Path(r"data_files/" + date_format + VERSION_CODE + ".txt")
    return filepath


def record_stop_playing():
    file_path = get_file_path()
    current_time_formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open(file_path, "a+") as f:
        f.write(f"Stopped playing at {current_time_formatted}\n")
        print(f"Stopped playing at {current_time_formatted}")


def record_start_playing(game_name):
    file_path = get_file_path()
    current_time_formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open(file_path, "a+") as f:
        f.write(f"Started playing {game_name} at {current_time_formatted}\n")
        print(f"Started playing {game_name} at {current_time_formatted}")