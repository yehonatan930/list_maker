import re
import sys

from files_util import get_oldest_log_with_show, get_good_episodes_filenames
from text_util import get_number_from_line
from user_interface import print_no_ep_error


class Show:
    def __init__(self, name, dir_path, current_appender, is_special_series=False):
        self.is_special_series = is_special_series
        self.name = name
        self.dir_path = dir_path

        self.ep_num_indexes = {}
        self.base_number = 0
        self.find_show_ep_number_indexes()
        self.find_show_base_number(current_appender)

        self.episodes_paths = []
        self.list_length = 0

    def set_episodes_paths(self, episodes_paths):
        self.episodes_paths = episodes_paths
        self.list_length = len(self.episodes_paths)

    def find_show_ep_number_indexes(self):
        filenames_in_folder = get_good_episodes_filenames(self.dir_path)

        try:
            first_filename = filenames_in_folder[0]
            second_filename = filenames_in_folder[1]
        except IndexError:
            print_no_ep_error(self.dir_path)
            sys.exit()

        for num_in_first, num_in_second in zip(re.finditer(r'\d+', first_filename),
                                               re.finditer(r'\d+', second_filename)):
            if ( num_in_first.group() == "01" and num_in_second.group() == "02") or (
                    num_in_first.group() == "001" and num_in_second.group() == "002") or (
                    num_in_first.group() == "0001" and num_in_second.group() == "0002"):
                self.ep_num_indexes = {"start_index": num_in_first.start(),
                                       "end_index": num_in_first.end()}

    def find_show_base_number(self, current_appender, current_appender_line_index=9):
        # base_number + current_appender = starting episode
        try:
            self.base_number = 0 - get_number_from_line(get_oldest_log_with_show(self)[current_appender_line_index])
        except (AttributeError, TypeError):
            self.base_number = 0 - current_appender
