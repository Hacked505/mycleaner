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
import os
from itertools import chain


class PathData:

    @staticmethod
    def __get_my_folder_obj(new_path):
        """Creates a folder object for storing paths to all nested files and folders.

        Accepts:
        ----------
        new_path - path to an existing folder

        Returns:
        -----------
        Class instance MyFolder
        """

        class MyFolder:
            """Used for storing the path to a folder

            and storing the paths to all files and folders attached to it.

            Important! When you add a folder, all files and folders attached to it will be added.
            Requires an existing folder path address when creating an instance.
            Stores the path address and allows you to get all subfolders and files recursively.

            Get attached files:
            get_files(self) -> iter:
            Get subfolders:
            get_folders(self) -> iter:
            Folder path:
            @property
            ath(self) -> str:
            """

            def __init__(self, path: str):
                if os.path.isdir(path):
                    self.__path = path
                else:
                    raise NotADirectoryError('Not Folder!')

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

    def __init__(self):
        self.__dirs = {}  # folder paths as instances of the MyFolder () class, where the key is the folder path.
        self.__files = set()  # Stores the paths to the files

    def add_path(self, path: str) -> bool:
        """Adds the path to a file or folder to temporary storage

        Important! When you add a folder, all files and folders attached to it will be added.

        Checks for the existence of a path, for the presence of duplicates,
        a "link". Adds to the desired repository,
        depending on type (file, folder).

        Parameters:
        ----------
        path - path to the file or folder

        Returns:
        -----------
        True/False
        Logical status of adding a path to a file or folder.
        """
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__files.add(path) if os.path.isfile(path) else self.__add_folder(path)
            return True
        return False

    def del_path(self, path: str) -> bool:
        """Deletes the path to a file or folder from temporary storage

        Removes a path from the repository. If a folder is deleted, the folder object is deleted,
        all nested paths are no longer taken into account losing relevance.

        Important! When you delete a folder from temporary storage,
        all files and folders attached to it will be deleted.

        Parameters:
        ----------
        path - path to the file or folder

        Returns:
        -----------
        True/False
        Returns the logical status of deleting the path to a file or folder.
        """
        if self.search_for_duplicates(path):
            if path in self.__dirs:
                del self.__dirs[path]
            elif path in self.__files:
                self.__files.remove(path)
            return True
        return False

    def get_files(self) -> iter:
        """Retrieves all added files from the storage, including those nested in all folders.

        Returns:
        -----------
        Returns a generator containing paths to all files.
        """
        return (i for i in chain(self.__files, (file for obj in self.__dirs.values() for file in obj.get_files())))

    def get_folders(self) -> iter:
        """Retrieves all added folders from the storage, including those nested in all folders.

        Returns:
        -----------
        Returns an iterator containing paths to all folders.
        """
        return reversed(sorted(path for obj in self.__dirs.values() for path in obj.get_folders()))

    @property
    def is_any_data(self) -> bool:
        """Checks for paths in the storage

        Returns:
        -----------
        True/False
        Returns the logical status of checking for the presence/absence of added paths."""
        if self.__files or self.__dirs:
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Checks for duplicates

        Returns:
        -----------
        True/False
        Returns the logical status of the duplicate path check."""
        return True if path in self.__dirs or path in self.__files else False

    def clear_data(self) -> None:
        """Cleans storage with paths"""
        self.__dirs.clear()
        self.__files.clear()

    def __add_folder(self, path: str) -> None:
        """Creates a new “folder” object

        Parameters:
        ----------
        path - path to the folder

        Saves it in storage, where the key is the path, and the value is the folder object.
        """
        self.__dirs[path] = self.__get_my_folder_obj(path)


def main():
    pass


if __name__ == '__main__':
    main()
