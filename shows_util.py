import glob
import os
import sys

from files_util import get_good_folders_paths, is_path_a_good_episode
from show import Show
from text_util import clean_string
from user_interface import get_chosen_subdirectory, print_info_messages, print_ep_num_error, \
    print_show_name_is_weird_error

ALL_SHOWS_FOLDER = r"D:\כרגע"
SPECIAL_SHOWS = ['boruto', 'bleach', "twelve"]


def find_ep_number(show, ep_path):
    name = os.path.basename(ep_path)
    if show.is_special_series:
        all_paths_in_folder = [os.path.join(
            show.dir_path, ep_p) for ep_p in os.listdir(show.dir_path)]
        return list(filter(lambda p: is_path_a_good_episode(p), all_paths_in_folder)).index(ep_path) + 1
    else:
        ep_indexes = show.ep_num_indexes

        try:
            return int(name[ep_indexes["start_index"]:ep_indexes["end_index"]])
        except (ValueError, TypeError, KeyError):
            print_ep_num_error(ep_path, ep_indexes)
            sys.exit()


def get_directories_for_shows():
    global ALL_SHOWS_FOLDER
    directories = []

    # old to new
    for show_dir in sorted(glob.glob(fr"{ALL_SHOWS_FOLDER}\*"), key=os.path.getctime):
        inner_show_dirs = get_good_folders_paths(show_dir)

        print(f"\n{show_dir} options:")
        if inner_show_dirs:
            chosen_show_directory = get_chosen_subdirectory(inner_show_dirs)
        else:
            chosen_show_directory = get_chosen_subdirectory([show_dir])

        if chosen_show_directory:
            directories.append(chosen_show_directory)

    return directories


def generate_shows(current_appender):
    global SPECIAL_SHOWS
    shows = []

    for sub_dir_index, sub_dir_path in enumerate(get_directories_for_shows()):

        show_episodes_paths = []
        name = find_show_name(sub_dir_path)

        is_special = any([(spsh in name) for spsh in SPECIAL_SHOWS])

        show = Show(name, sub_dir_path, current_appender, is_special)

        print_info_messages('g', show.name)

        for root, dirs, files in os.walk(sub_dir_path):
            for filename in files:
                episode_path = os.path.join(root, filename)
                start_episode = current_appender + show.base_number
                if is_path_a_good_episode(episode_path) and find_ep_number(show, episode_path) > start_episode:
                    show_episodes_paths.append(episode_path)

        if show_episodes_paths:
            show.set_episodes_paths(show_episodes_paths)
            shows.append(show)

    return shows


def find_show_name(show_folder_path):
    global ALL_SHOWS_FOLDER

    parent_folder = os.path.dirname(show_folder_path)
    if parent_folder == ALL_SHOWS_FOLDER:
        show_folder_name = os.path.basename(show_folder_path)
        appendix = ""
    else:
        show_folder_name = os.path.basename(parent_folder)
        subfolders = [os.path.join(parent_folder, file)
                      for file in os.listdir(parent_folder)
                      if os.path.isdir(os.path.join(parent_folder, file))
                      and ".unwanted" not in os.path.join(parent_folder, file)]

        appendix = str(subfolders.index(show_folder_path) + 1)

    function_words = ['', 'the', 'a', 'an', 'he', 'him', 'she', 'her', 'I', 'my', 'mine', 'your', 'you', 'and', 'that',
                      'this', 'they', 'is', 'am', 'are', 'when', 'while', 'no', 'not', 'nor', 'as', 'or', 'of', 'at',
                      'in', 'without', 'between', 'have', 'has', 'got', 'do', 'but', 'if', 'then', 'well', 'however',
                      'would', 'could', 'should', 'yes', 'no', 'to', "from"]
    try:
        show_name = [name_part
                     for name_part in clean_string(show_folder_name).lower().split(" ")
                     if name_part not in function_words][0]

        return show_name + appendix
    except IndexError:
        print_show_name_is_weird_error(show_folder_name)
        sys.exit()


def make_final_list(shows, minimum_show_length):
    final_paths_list = []

    for ep_round_index in range(minimum_show_length):
        for show in shows:
            final_paths_list.append(show.episodes_paths[ep_round_index])

    print("finalized list created.")

    return final_paths_list
