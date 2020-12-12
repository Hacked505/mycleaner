# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Aleksandr Suvorov
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/mycleaner/
# -----------------------------------------------------------------------------
"""Module for working with file and folder paths.

Adding, deleting, getting and storing paths to files and folders,
as well as checking for duplicates, checking for the presence of paths, their existence, etc
.is Used as an auxiliary module for convenient work with paths to files and folders
before destroying them, zeroing data, deleting.
"""
import os
from itertools import chain
from pathlib import Path


class PathObj:
    """Creates a path object for the file or folder."""
    def __init__(self, path: str):
        """When creating an object, you must specify a path that is checked for existence."""
        self.__path = path

    @property
    def path(self):
        """Path to the file or folder"""
        return self.__path

    def get_files(self) -> iter:
        """Returns the file path generator"""
        if Path(self.__path).is_file():
            return [self.__path]
        elif Path(self.__path).is_dir():
            return (file for file in [os.path.join(p, f)
                                      for p, _, files in os.walk(self.__path)
                                      for f in files])


class Folder:
    """Creates a folder object"""
    def __init__(self, path: str):
        """When creating an object, you must specify a verified path to the folder"""
        if Path(path).is_dir():
            self.__path = path
        else:
            raise NotADirectoryError('Not Folder!')

    def get_files(self) -> iter:
        """Returns the file path generator"""
        return (os.path.join(p, file) for p, _, files in os.walk(self.__path) for file in files)

    def get_folders(self) -> iter:
        """Returns the folder path generator"""
        return (os.path.join(p, d) for p, dirs, _ in os.walk(self.__path) for d in dirs)

    @property
    def path(self) -> str:
        """Path to the file or folder"""
        return self.__path


class DataObj:
    """Creates an object for working with file and folder paths"""
    def __init__(self):
        self.__dirs = {}
        self.__files = set()

    def add_path(self, path: str) -> bool:
        """Adding a path

        Check for the existence of the distribution on the desired data structures.
        If the path is to a folder, creates a folder object and adds it to the path store.
        """
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__files.add(path) if os.path.isfile(path) else self.__add_folder(path)
            return True
        return False

    def del_path(self, path: str) -> bool:
        """Deleting a path

        If the path to a folder, deletes the folder object(all paths to
        files and folders located inside the folder are deleted accordingly.
        """
        if self.search_for_duplicates(path):
            if path in self.__dirs:
                del self.__dirs[path]
            elif path in self.__files:
                self.__files.remove(path)
            return True
        return False

    def get_files(self) -> iter:
        """Returns a generator with file paths from all objects"""
        return (i for i in chain(self.__files, (file for obj in self.__dirs.values() for file in obj.get_files())))

    def get_folders(self) -> iter:
        """Getting folders"""
        return reversed(sorted(path for obj in self.__dirs.values() for path in obj.get_folders()))

    @property
    def is_any_data(self) -> bool:
        """Checking for data in repositories"""
        if self.__files or self.__dirs:
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Checking for duplicates"""
        return True if path in self.__dirs or path in self.__files else False

    def clear_data(self) -> None:
        """Clearing storage"""
        self.__dirs.clear()
        self.__files.clear()

    def __add_folder(self, path: str) -> None:
        """Creating a folder object and adding it to the storage"""
        self.__dirs[path] = Folder(path)
