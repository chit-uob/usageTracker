# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time

import process_checker
import file_manipulation


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    was_previously_playing = False
    while True:
        is_playing = process_checker.check_if_process_is_running("t2gp.exe")
        if is_playing != was_previously_playing:
            if is_playing:
                file_manipulation.record_start_playing()
            else:
                file_manipulation.record_stop_playing()
        time.sleep(10)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
