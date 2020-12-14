# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Aleksandr Suvorov
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/mycleaner/
# -----------------------------------------------------------------------------
"""Console utility for destroying, zeroing, and deleting files.


"""
import argparse
import sys
import shutil
import os
from pathlib import Path
from mycleaner import cleaner
from mycleaner.smart import PathObj
from mycleaner import __version__


COLUMNS, _ = shutil.get_terminal_size()
VERSION = f'v{__version__}'


def get_num_files(path):
    if Path(path).is_dir():
        return sum([len(files) for _, _, files in os.walk(path)])
    elif Path(path).is_file():
        return 1
    else:
        return 0


def logo_start():
    print('My Cleaner'.center(COLUMNS, '='))
    print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
    print('Utility for mashing, zeroing, deleting files'.center(COLUMNS, '='))


def logo_end():
    print(''.center(COLUMNS, '='))
    print('The program is complete'.center(COLUMNS, '-'))


def get_path():
    if len(sys.argv) > 1:
        return [path for path in sys.argv[1:] if Path(path).exists() and (Path(path).is_file() or Path(path).is_dir())]


def logo_dec(func):
    def deco():
        print('My Cleaner'.center(COLUMNS, '='))
        print('Aleksandr Suvorov | myhackband@ya.ru'.center(COLUMNS, '-'))
        print('Utility for mashing, zeroing, deleting files'.center(COLUMNS, '='))
        func()
        print(''.center(COLUMNS, '='))
        print('The program is complete'.center(COLUMNS, '-'))
    return deco


def make_error_log(error_list):
    print(f'Errors: {len(error_list)}')
    with open('term_my_cleaner_error_log.txt', 'wt') as f:
        print('Errors'.center(COLUMNS, '='), file=f)
        for err in error_list:
            print(err, file=f)
    print(f'Save term_my_cleaner_error_log.txt')


def createParser():
    parser = argparse.ArgumentParser(
        description='A package of modules and console utilities for destroying, zeroing, and deleting files',
        prog='My Cleaner',
        epilog="""Email: myhackband@ya.ru""",
    )
    parser.add_argument('paths', nargs='+', help='Space-separated paths to files and folders')
    parser.add_argument('--log', help='Save errors log',
                        action='store_const', const=True, default=False)
    parser.add_argument('--version', action='version', help='Program version', version='%(prog)s {}'.format(VERSION))
    return parser


def check_path(path_list):
    return [path for path in path_list if Path(path).exists()]


def destroy(obj, file):
    print(f'Destroying the file: {file}')
    return obj.shred_file(file)


def zero(obj, file):
    print(f'Resetting the file: {file}')
    return obj.zero_file(file)


def delete(obj, file):
    print(f'Delete files: {file}')
    return obj.del_file(file)


def start(obj_dict, method=1, log=False):
    error_list = []
    my_cleaner = cleaner.Cleaner()
    while True:
        try:
            my_cleaner.shreds = int(input('Enter the number of overwrites for files: '))
        except ValueError:
            my_cleaner.shreds = 30
        break
    for obj in obj_dict.values():
        status = None
        print(f'Working with: {obj.path}'.center(COLUMNS, '='))
        for file in obj.get_files():
            if method == 1:
                status = destroy(my_cleaner, file=file)
            elif method == 2:
                status = zero(my_cleaner, file=file)
            elif method == 3:
                status = delete(my_cleaner, file=file)
            if not status:
                error_list.append(file)
    print('The work has been completed'.center(COLUMNS, '='))
    print(f'Files were processed: {my_cleaner.count_del_files + my_cleaner.count_zero_files}')
    print(f'Errors: {len(error_list)}')
    if log:
        make_error_log(error_list)


def make_path_obj(path_list):
    if path_list:
        obj_dict = {n: PathObj(path) for n, path in enumerate(path_list, 1)}
        print(''.center(COLUMNS, '-'))
        return obj_dict
    else:
        return False


def main():
    parser = createParser()
    namespace = parser.parse_args()
    logo_start()
    arg_list = namespace.paths
    path_list = check_path(arg_list)
    print(f'Paths added: {len(path_list)}')
    obj_dict = make_path_obj(path_list)
    if obj_dict:
        print(f'Counting files...')
        for key, val in obj_dict.items():
            print(f'{key}: path: {val.path} | files[{val.num_files}]')
        print(f''.center(COLUMNS, '-'))
        while True:
            num_files = sum(obj.num_files for obj in obj_dict.values())
            if not num_files:
                print('Nothing found...')
                break
            print('Select the desired action:\n0. Exit\n1. Destruction and delete\n2. '
                  'Zeroing not delete\n3. Zeroing and delete')
            print(''.center(COLUMNS, '-'))
            try:
                user_input = int(input('Input: '))
                if user_input not in [0, 1, 2, 3]:
                    raise ValueError
            except ValueError:
                print(''.center(COLUMNS, '-'))
                print('Input error!')
                continue
            else:
                start(obj_dict=obj_dict, method=user_input, log=namespace.log)
            break
    else:
        print('Error! You haven\'t added a path...')
    logo_end()


if __name__ == '__main__':
    main()
