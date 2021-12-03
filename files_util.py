import glob
import os
import re

from text_util import un_bold, get_number_from_line
from user_interface import input_custom_length, list_version_input

LISTS_FOLDER = r"D:\רשימות"
LOGS_FOLDER = r"D:\רשימות\logs"
LOGS_BY_CREATION_TIME = sorted(glob.glob(fr"{LOGS_FOLDER}\*"), key=os.path.getctime)  # old to new


def write_log_to_file(log, list_version):
    global LOGS_FOLDER
    with open(fr"{LOGS_FOLDER}\{list_version}.txt", mode="w", encoding="utf-8") as f:
        f.write(un_bold(log))


def write_list_to_file(list_version, paths_list):
    global LISTS_FOLDER
    with open(fr"{LISTS_FOLDER}\list_{list_version}.m3u", mode="w", encoding="utf-8") as m3u_list_file:
        m3u_list_file.write("\n".join(paths_list))


def get_current_appender(ep_rounds_line_index=6, current_appender_line_index=9):
    global LOGS_BY_CREATION_TIME
    # current appender = previous appender + previous eps rounds

    custom_last_list_ep_rounds_amount = input_custom_length()

    with open(LOGS_BY_CREATION_TIME[-1], mode="r", encoding="utf-8") as latest_log_file:
        latest_log = latest_log_file.readlines()

        if custom_last_list_ep_rounds_amount.isdigit():
            last_list_ep_rounds_amount = int(custom_last_list_ep_rounds_amount)
        else:
            last_list_ep_rounds_amount = get_number_from_line(latest_log[ep_rounds_line_index])

        return last_list_ep_rounds_amount + get_number_from_line(latest_log[current_appender_line_index])


def get_oldest_log_with_show(show):
    global LOGS_BY_CREATION_TIME
    for log_path in LOGS_BY_CREATION_TIME:
        with open(log_path, mode="r", encoding="utf-8") as log_file:
            log = log_file.read()

            if show.name in log and os.path.getctime(log_path) >= os.path.getctime(show.dir_path):
                return log.split('\n')


def get_list_version():
    global LOGS_BY_CREATION_TIME
    latest_log_name = LOGS_BY_CREATION_TIME[-1]
    numbers = re.search(r'(\d+)-(\d+)', latest_log_name)
    list_number = int(numbers.group(1))
    version_number = int(numbers.group(2))

    list_number, version_number = list_version_input(list_number, version_number)

    return f"{list_number}-{version_number}"


def is_path_a_good_folder(folder_path):
    return os.path.isdir(folder_path) and ".unwanted" not in folder_path


def get_good_folders_paths(parent_folder_path):
    return [os.path.join(parent_folder_path, folder_name)
            for folder_name in os.listdir(parent_folder_path)
            if is_path_a_good_folder(os.path.join(parent_folder_path, folder_name))]


def is_path_a_good_episode(episode_path):
    return os.path.isfile(episode_path) and episode_path.endswith(
        (".mkv", ".avi", ".mp4")) and ".unwanted" not in episode_path


def get_good_episodes_filenames(folder_path):
    return [file for root, folders, files in os.walk(folder_path) for file in files if
            is_path_a_good_episode(os.path.join(root, file))]
