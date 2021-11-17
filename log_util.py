from shows_util import find_ep_number
from text_util import bold
from user_interface import print_info_messages


def make_current_log(current_appender, ep_rounds_amount, shows, final_paths_list, current_time, list_version):
    divider = "=" * 150

    episodes_left_table = "{:<30} {:<60} {}\n{}\n" \
        .format(bold("SHOW"),
                bold("EPS REMAINING BEFORE LIST") + " | list's first episode",
                bold("EPS REMAINING AFTER LIST") + " | list's last episode",
                divider)

    for show_index, show in enumerate(shows):
        print_info_messages('i', show.name)

        name = f"{str(show_index + 1).zfill(2)}. {show.name + ':':<42}"
        eps_remaining_before_list = f"{str(show.list_length):<3}"
        eps_remaining_after_list = f"{str(show.list_length - ep_rounds_amount):<3}"
        first_ep_in_list = f"| {str(find_ep_number(show, show.episodes_paths[0])):<47}"
        last_ep_in_list = f"| {str(find_ep_number(show, show.episodes_paths[ep_rounds_amount - 1])):<3}"

        episodes_left_table += f"{bold(name)}" \
                               f"{bold(eps_remaining_before_list)}{first_ep_in_list}" \
                               f"{bold(eps_remaining_after_list)}{last_ep_in_list} "

        if show.list_length - ep_rounds_amount == 0:
            episodes_left_table += bold(f"{' OVER ':+^43}")

        episodes_left_table += '\n'

    eps_paths_list = ""
    for show_index in range(len(final_paths_list)):
        if show_index % len(shows) == 0:
            # end of episodes round
            eps_paths_list += "-" * 150 + "\n"
        eps_paths_list += final_paths_list[show_index] + "\n"

    base_numbers = [show.base_number for show in shows if show.name != 'specials']

    return f"\n" \
           f"DATE: {str(current_time)}\n" \
           f"{divider}\n" \
           f"LIST No.: {list_version}\n" \
           f"{divider}\n" \
           f"NUMBER OF SHOWS: {len(shows)}\n" \
           f"EPISODES ROUNDS: {ep_rounds_amount}\n" \
           f"{divider}\n" \
           f"BASE NUMBERS: {base_numbers}\n" \
           f"CURRENT APPENDER: {current_appender}\n" \
           f"{divider}\n" \
           f"{bold('EPISODES LEFT')}:\n" \
           f"{episodes_left_table}\n" \
           f"{divider}\nLIST: \n" \
           f"{eps_paths_list}"
