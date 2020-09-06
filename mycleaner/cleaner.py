#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Aleksandr Suvorov
# Yandex Money: https://money.yandex.ru/to/4100110928527458
# Sberbank Russia: 4276 4417 5763 7686
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/mycleaner/
# PyPi: https://pypi.org/project/mycleaner/
# -----------------------------------------------------------------------------
"""cleaner.py - API module for destroying, zeroing and deleting files"""
import os
from random import randint
from itertools import chain


class Cleaner:
    """Mashing, zeroing, and deleting files/folders."""

    def __init__(self):
        self.__dirs = {}  # folder paths as instances of the MyFolder () class, where the key is the folder path.
        self.__files = set()  # Stores the paths to the files
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    def add_path(self, path: str) -> bool:
        """Returns the logical status of adding a path to a file or folder.

        Checks for the existence of a path, for the presence of duplicates, a "link". Adds to the desired repository,
        depending on type (file, folder).
        """
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__files.add(path) if os.path.isfile(path) else self.__add_folder(path)
            return True
        return False

    def del_path(self, path: str) -> bool:
        """Returns the logical status of deleting the path to a file or folder.

        Removes a path from the repository. If a folder is deleted, the folder object is deleted,
        all nested paths are no longer taken into account losing relevance.
        """
        if self.search_for_duplicates(path):
            if path in self.__dirs:
                del self.__dirs[path]
            elif path in self.__files:
                self.__files.remove(path)
            return True
        return False

    def get_files_gen(self) -> iter:
        """Returns a generator containing paths to all files.

        Including files attached to folders,
        objects that were added to the storage.
        """
        return (i for i in chain(self.__files, (file for obj in self.__dirs.values() for file in obj.get_files())))

    def get_folders_gen(self) -> iter:
        """Returns an iterator containing paths to all files.

        Including files attached to folders,
        objects that were added to the storage .
        """
        return reversed(sorted(path for obj in self.__dirs.values() for path in obj.get_folders()))

    @property
    def is_any_data(self) -> bool:
        """Returns the logical status of checking for the presence / absence of added paths."""
        if self.__files or self.__dirs:
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Returns the logical status of the duplicate path check."""
        return True if path in self.__dirs or path in self.__files else False

    def clear_data(self) -> None:
        """Cleans storage with paths"""
        self.__dirs.clear()
        self.__files.clear()

    def __add_folder(self, path: str) -> None:
        """Creates a new “folder” object, saves it in storage,


        where the key is the path, and the value is the folder object
        """
        self.__dirs[path] = self.__get_obj(path)

    @staticmethod
    def __get_obj(new_path):

        class MyFolder:
            """MyFolder object

            When creating an instance, it requires an existing folder path address.
            Stores the path address, allows you to get recursively.
            """
            def __init__(self, path: str):
                if os.path.isdir(path):
                    self.__path = path
                else:
                    raise NotADirectoryError('Not Folder!!!')

            def get_files(self) -> iter:
                """Returns a generator containing paths to all nested files."""
                return (os.path.join(p, file) for p, _, files in os.walk(self.__path) for file in files)

            def get_folders(self) -> iter:
                """Returns a generator containing paths to all nested folders."""
                return (os.path.join(p, d) for p, dirs, _ in os.walk(self.__path) for d in dirs)

            @property
            def path(self) -> str:
                """Returns the path to the folder whose data is stored in the object."""
                return self.__path
        return MyFolder(new_path)

    @staticmethod
    def replace_path(path: str) -> str:
        """Linux path escaping"""
        symbol = ' !$^&*()=|[]{}?,<>"\':`;'
        for s in symbol:
            if s in path:
                path = path.replace(s, f'\\{s}')
        return path

    def zero_file(self, file: str) -> bool:
        """Resets the file. Return the logical result of zeroing the file"""
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, path: str, shreds: int) -> bool:
        """Overwrites the file with random data and deletes it.

        Returns the logical status of file overwriting.
        Overwrites and deletes the file using the desired method for a specific platform.
        """
        if os.name == 'posix':
            file = self.replace_path(path)
            os.system(f'shred -zvu -n {shreds} {file}')
        else:
            try:
                for i in range(shreds):
                    with open(path, 'wb') as f:
                        f.write(bytes(i * randint(1, 1000)))
                        f.flush()
                os.remove(path)
                with open(path, 'wb') as f:
                    f.write(bytes(0))
                os.remove(path)
            except OSError:
                return False
        if not os.path.exists(path):
            self.count_del_files += 1
            return True
        return False

    def del_file(self, path: str) -> bool:
        """Deletes the file in the usual way, returns status."""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                os.remove(path)
        except OSError:
            return False
        if not os.path.exists(path):
            self.count_del_files += 1
            return True
        return False

    def del_dir(self, path: str) -> bool:
        """Deletes a folder, returns status."""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                os.rmdir(path)
        except OSError:
            return False
        if not os.path.exists(path):
            self.count_del_dirs += 1
            return True
        return False

    def reset_count(self) -> None:
        """Resets counters to 0"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0


def main():
    pass


if __name__ == '__main__':
    main()
