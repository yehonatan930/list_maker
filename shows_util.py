import glob
import os
import sys

from show import Show
from text_util import is_path_a_good_episode, clean_string
from user_interface import get_chosen_subdirectory, print_info_messages, print_ep_num_error

SHOWS_FOLDER = r"D:\כרגע"


def find_ep_number(show, ep_path):
    ep_indexes = show.ep_num_indexes
    name = os.path.basename(ep_path)

    try:
        return int(name[ep_indexes["start_index"]:ep_indexes["end_index"]])
    except (ValueError, TypeError, KeyError):
        print_ep_num_error(ep_path, ep_indexes)
        sys.exit()


def get_directories_for_shows():
    global SHOWS_FOLDER
    directories = []

    for subdirectory_path in sorted(glob.glob(fr"{SHOWS_FOLDER}\*"), key=os.path.getctime):
        sub_subdirectories_paths = [os.path.join(subdirectory_path, folder_name) for folder_name in
                                    os.listdir(subdirectory_path) if
                                    os.path.isdir(os.path.join(subdirectory_path, folder_name)) and
                                    ".unwanted" != folder_name]

        print(f"\n{subdirectory_path} options:")
        if sub_subdirectories_paths:
            chosen_show_directory = get_chosen_subdirectory(sub_subdirectories_paths)
        else:
            chosen_show_directory = get_chosen_subdirectory([subdirectory_path])

        if chosen_show_directory:
            directories.append(chosen_show_directory)

    print("\n")

    return directories


def generate_shows(current_appender):
    shows = []

    for sub_dir_index, sub_dir_path in enumerate(get_directories_for_shows()):

        show_episodes_paths = []

        show = Show(find_show_name(sub_dir_path), sub_dir_path, current_appender)

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
    global SHOWS_FOLDER

    parent_folder = os.path.dirname(show_folder_path)
    if parent_folder == SHOWS_FOLDER:
        show_folder_name = os.path.basename(show_folder_path)
        appendix = ""
    else:
        show_folder_name = os.path.basename(parent_folder)
        appendix = str(os.listdir(parent_folder).index(os.path.basename(show_folder_path)) + 1)

    clean_folder_name = clean_string(show_folder_name)

    show_name = [name_part for name_part in clean_folder_name.split(" ") if name_part != ''][0].lower()

    return show_name + appendix


def make_final_list(shows, minimum_show_length):
    final_paths_list = []

    for ep_round_index in range(minimum_show_length):
        for show in shows:
            final_paths_list.append(show.episodes_paths[ep_round_index])

    print("finalized list created.")

    return final_paths_list


def get_good_episodes_filenames(dir):
    filenames_in_folder = []
    for root, folders, files in os.walk(dir):
        for file in files:
            if is_path_a_good_episode(os.path.join(root, file)):
                filenames_in_folder.append(file)
    return filenames_in_folder
