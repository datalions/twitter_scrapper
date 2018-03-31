from pathlib import Path
from os import listdir


def take_auth_data():
    """
    Works properly if all files with access tokens are placed inside Documents/twitter/keys folder
    :return: Dictionary with pairs {'Token type': 'Token value'}
    """
    home = str(Path.home())
    path_to_keys = '/Documents/twitter/keys/'

    files = [f for f in listdir(home+path_to_keys) if '.DS' not in f]

    tokens = []
    for f in files:
        with open(home+path_to_keys+f, 'r') as lines:
            ln = lines.readline().replace(" ", "")
            tokens.append(ln)

    auth_data = dict(zip(files, tokens))
    return auth_data


def take_search_words(folder):
    """
    Works properly if all files with words to search are placed inside Documents/twitter/topics folder
    :param folder: folder with files with words
    :return: Array of words for searching process
    """
    words = []

    list_of_files = [f for f in listdir(folder) if f[-4:] == '.txt']

    for textfile in list_of_files:
        with open(folder + textfile, 'r') as my_file:
            for line in my_file:
                ln = line.strip()
                words.append(ln)

    return words


if __name__ == '__main__':
    testcase = take_auth_data()
    testcase2 = take_search_words('test')
