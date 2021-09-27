import os

from main import find_show_ep_number_indexes


def rename_all_files_in_folder(folder):
    episodes_paths = []
    print(os.listdir(folder))
    input("\ncontinue?")
    for root, dirs, files in os.walk(folder):
        for name in files:
            if name.endswith((".mkv", ".avi", ".mp4")) and \
                    ".unwanted" not in root:
                episodes_paths.append(os.path.join(root, name))
    print("\n")
    print("\n".join(episodes_paths))
    input("\ncontinue?")

    enp = find_show_ep_number_indexes(folder)

    for i, path in enumerate(episodes_paths):
        new_name = os.path.basename(path)[:enp["start_index"] - 1]
        new_name += "⟨⟨⟨{}⟩⟩⟩".format(str(i + 1).zfill(enp["length"]))
        new_name += os.path.basename(path)[enp["start_index"]:]
        old_dir = os.path.dirname(path)
        print(new_name)
        os.rename(path, os.path.join(old_dir, new_name))


def tt(path):
    return [f.path for f in os.scandir(r"D:\כרגע\[Aeenald] Himouto! Umaru-chan [BDRip 1080p HEVC-10bit Opus]") if f.is_dir()]


if __name__ == '__main__':

    # print([f.path for f in os.scandir(r"D:\כרגע\[Aeenald] Himouto! Umaru-chan [BDRip 1080p HEVC-10bit Opus]") if f.is_dir()])
    # print(glob.glob(r"D:\כרגע\[Judas] Seraph of the End (Seasons 1-2) [BD 1080p][HEVC x265 10bit][Dual-Audio][Eng-Subs]\*"))
    # print("\n".join(get_directories_for_shows()))
    a = ['a']
    a.append([])
    print(a)