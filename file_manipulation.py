# To save/get data from file
import pathlib
from datetime import datetime


def get_file_path():
    date_format = datetime.now().strftime("%Y%m%d")
    filepath = pathlib.Path(r"data_files/" + date_format + ".txt")
    return filepath


def record_stop_playing():
    file_path = get_file_path()
    current_time_formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open(file_path, "a+") as f:
        f.write(f"Stopped playing at {current_time_formatted}\n")
        print(f"Stopped playing at {current_time_formatted}")


def record_start_playing():
    file_path = get_file_path()
    current_time_formatted = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    with open(file_path, "a+") as f:
        f.write(f"Started playing at {current_time_formatted}\n")
        print(f"Started playing at {current_time_formatted}")