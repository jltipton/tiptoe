import os


def list_files(folder_path):
    list_of_files = list()
    for (dirpath, dirnames, filenames) in os.walk(folder_path):
        list_of_files += [os.path.join(dirpath, file) for file in filenames]
    return list_of_files


def setup_path(folder_path):
    if not os.path.exists(folder_path):
        try:
            os.makedirs(folder_path)
        except OSError:
            logging.info('failed to create {}'.format(folder_path))
        else:
            logging.info('created directory(s) {}'.format(folder_path))
    return folder_path


