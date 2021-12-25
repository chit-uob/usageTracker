# to check what processes are running
import psutil as psutil


def check_what_processes_are_running():
    processes_list = []
    for proc in psutil.process_iter():
        processes_list.append(proc.name())
    return processes_list


def check_if_process_is_running(process_name):
    for proc in psutil.process_iter():
        if proc.name().lower() == process_name.lower():
            return True
    return False


def check_what_games_are_running(process_dict):
    process_list = []
    for key in process_dict.keys():
        if check_if_process_is_running(key):
            process_list.append(process_dict[key])
    return process_list
