import glob
import os
import re

from text_util import un_bold, get_number_from_line
from user_interface import input_custom_length, list_version_input

LISTS_FOLDER = r"D:\רשימות"
LOGS_FOLDER = r"D:\רשימות\logs"


def write_log_to_file(log, list_version):
    global LOGS_FOLDER
    with open(fr"{LOGS_FOLDER}\{list_version}.txt", mode="w", encoding="utf-8") as f:
        f.write(un_bold(log))


def write_list_to_file(list_version, paths_list):
    global LISTS_FOLDER
    with open(fr"{LISTS_FOLDER}\list_{list_version}.m3u", mode="w", encoding="utf-8") as m3u_list_file:
        m3u_list_file.write("\n".join(paths_list))


def get_current_appender(ep_rounds_line_index=6, current_appender_line_index=9):
    global LOGS_FOLDER
    # current appender = previous appender + previous eps rounds

    custom_last_list_ep_rounds_amount = input_custom_length()

    with open(sorted(glob.glob(fr"{LOGS_FOLDER}\*"), key=os.path.getctime)[-1], mode="r",
              encoding="utf-8") as latest_log_file:
        latest_log = latest_log_file.readlines()

        if custom_last_list_ep_rounds_amount.isdigit():
            last_list_ep_rounds_amount = int(custom_last_list_ep_rounds_amount)
        else:
            last_list_ep_rounds_amount = get_number_from_line(latest_log[ep_rounds_line_index])

        return last_list_ep_rounds_amount + get_number_from_line(latest_log[current_appender_line_index])


def get_oldest_log(show):
    global LOGS_FOLDER
    for log_path in sorted(glob.glob(fr"{LOGS_FOLDER}\*"), key=os.path.getctime):
        with open(log_path, mode="r", encoding="utf-8") as log_file:
            log = log_file.read()

            if show.name in log and os.path.getctime(log_path) >= os.path.getctime(show.dir_path):
                return log.split('\n')


def get_list_version():
    global LOGS_FOLDER
    latest_log_name = sorted(glob.glob(fr"{LOGS_FOLDER}\*"), key=os.path.getctime)[-1]
    numbers = re.search(r'(\d+)-(\d+)', latest_log_name)
    list_number = int(numbers.group(1))
    version_number = int(numbers.group(2))

    list_number, version_number = list_version_input(list_number, version_number)

    return f"{list_number}-{version_number}"
