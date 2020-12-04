# -----------------------------------------------------------------------------
# Copyright © 2020 Aleksandr Suvorov
# Licensed under the terms of the MIT License
# (see LICENSE.txt for details)
# -----------------------------------------------------------------------------
# Aleksandr Suvorov
# Email: myhackband@yandex.ru
# Github: https://github.com/mysmarthub/mycleaner/
# -----------------------------------------------------------------------------
import os
from itertools import chain
from pathlib import Path


class PathObj:
    def __init__(self, path):
        self.__path = path

    @property
    def path(self):
        return self.__path

    def get_files(self):
        if Path(self.__path).is_file():
            return [self.__path]
        elif Path(self.__path).is_dir():
            return (file for file in [os.path.join(p, f) for p, _, files in os.walk(self.__path) for f in files])


class Folder:
    def __init__(self, path: str):
        if os.path.isdir(path):
            self.__path = path
        else:
            raise NotADirectoryError('Not Folder!')

    def get_files(self) -> iter:
        return (os.path.join(p, file) for p, _, files in os.walk(self.__path) for file in files)

    def get_folders(self) -> iter:
        return (os.path.join(p, d) for p, dirs, _ in os.walk(self.__path) for d in dirs)

    @property
    def path(self) -> str:
        return self.__path


class DataObj:
    def __init__(self):
        self.__dirs = {}
        self.__files = set()

    def add_path(self, path: str) -> bool:
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__files.add(path) if os.path.isfile(path) else self.__add_folder(path)
            return True
        return False

    def del_path(self, path: str) -> bool:
        if self.search_for_duplicates(path):
            if path in self.__dirs:
                del self.__dirs[path]
            elif path in self.__files:
                self.__files.remove(path)
            return True
        return False

    def get_files(self) -> iter:
        return (i for i in chain(self.__files, (file for obj in self.__dirs.values() for file in obj.get_files())))

    def get_folders(self) -> iter:
        return reversed(sorted(path for obj in self.__dirs.values() for path in obj.get_folders()))

    @property
    def is_any_data(self) -> bool:
        if self.__files or self.__dirs:
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        return True if path in self.__dirs or path in self.__files else False

    def clear_data(self) -> None:
        self.__dirs.clear()
        self.__files.clear()

    def __add_folder(self, path: str) -> None:
        self.__dirs[path] = Folder(path)