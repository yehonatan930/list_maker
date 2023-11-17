import os


def oswalk(path):
    return os.walk(path)


def walk(path, level=0, only=''):
    i = 0
    for root, dirs, files in oswalk(path):
        if only != 'f':
            for subdirname in dirs :
                print(subdirname)
        if only != 'd':
            for filename in files:
                print(filename)

        i += 1
        if i == level:
            break


walk(r'D:\כרגע\Kono Oto Tomare!', 2, 'd')
