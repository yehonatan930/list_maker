import re


def bold(string):
    return '\033[1m' + string + '\033[0m'


def un_bold(string):
    return string.replace("\033[1m", "").replace("\033[0m", "")


def get_number_from_line(line, result_index=0):
    return int(re.findall(r'\d+', line)[result_index])


def clean_string(string):
    string_without_parenthesis = re.sub(r"(\[[^]]+])", "", string)
    string_without_parenthesis = re.sub(r"(\([^)]+\))", "", string_without_parenthesis)
    string_without_parenthesis = re.sub(r"({[^}]+})", "", string_without_parenthesis)
    clean_str = re.sub(r"[\\(){}\[\]~!@#$%^&*+/=<>;'|:?.,_-]", " ", string_without_parenthesis)
    return clean_str


def is_path_a_good_episode(episode_path):
    return episode_path.endswith((".mkv", ".avi", ".mp4")) and ".unwanted" not in episode_path
