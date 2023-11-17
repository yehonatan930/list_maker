from text_util import bold, red


def print_start_text():
    print("""remember: 
                    1. to move the show folders to כרגע.
                    2. to delete specials and movies.
                    3. delete folder from כרגע if remained
                    4. check for specials etc. in new shows folder.""")
    input("\nrestart now. if not needed press anything.       ")


def list_version_input(list_number, version_number):
    while True:
        action = input("\nnew list or new list version or rewrite last list version? [l/v/r]     ")
        if action == 'l':
            list_number += 1
            version_number = 0
            break
        elif action == 'v':
            version_number += 1
            break
        elif action == 'r':
            break
        else:
            print("bad option")
    return list_number, version_number


def input_custom_length():
    return input("\nset custom value for the last list's length? [yes - int/no - char]  ")


def get_chosen_subdirectory(sub_subdirectories_paths):
    print("\t0. skip show")

    for index, directory in enumerate(sub_subdirectories_paths):
        print(f"\t{index + 1}. {directory}")

    chosen_index = int(input("choose by number: "))
    print("\n")

    if chosen_index != 0:
        return sub_subdirectories_paths[chosen_index - 1]


def print_info_messages(message_type, show_name):
    if message_type == 'g':
        print(f"Generating {show_name} paths...")
    if message_type == 'i':
        print(f"Inserting {show_name} to log...")


def print_log(log):
    split_log = log.split('\n')
    line_index_until_list = split_log.index("LIST: ")

    for line in split_log[:line_index_until_list - 1]:
        print(line)

    if input("Print list? [y/n]    ") == 'y':
        for line in split_log[line_index_until_list:]:
            print(line)


def print_ep_num_error(ep_path, ep_indexes):
    print(bold(red(f"problem with: {ep_path}\nep_indexes: {ep_indexes}")))


def print_no_ep_error(folder_path):
    print(bold(red(f"First episodes not found in {folder_path}")))


def print_show_name_is_weird_error(show_folder_name):
    print(bold(red(f"Show's name is weird: {show_folder_name}")))
