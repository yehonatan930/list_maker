# -*- coding: utf-8 -*-
import warnings
from datetime import datetime

from files_util import write_log_to_file, write_list_to_file, get_current_appender, get_list_version
from log_util import make_current_log
from shows_util import generate_shows, make_final_list
from user_interface import print_start_text, print_log

warnings.filterwarnings('ignore', category=FutureWarning)


# todo: add special possbiblity
# todo: pre scan folder
# todo: add alerting before running
# todo: add saving shows in list
# todo: add gui

def run():
    print_start_text()

    current_time = datetime.now().strftime("%d.%m.%Y,    %H:%M:%S")

    list_version = get_list_version()

    current_appender = get_current_appender()

    shows = generate_shows(current_appender)

    shortest_list_length = min(shows, key=lambda show: show.list_length).list_length
    final_paths_list = make_final_list(shows, shortest_list_length)
    final_log = make_current_log(current_appender, shortest_list_length, shows, final_paths_list, current_time,
                                 list_version)

    write_log_to_file(final_log, list_version)
    write_list_to_file(list_version, final_paths_list)
    print_log(final_log)

    print("\nDone")


if __name__ == '__main__':
    run()
