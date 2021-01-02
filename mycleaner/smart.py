#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
import os
from pathlib import Path


class PathObj:
    """Creates a path object for the file or folder."""

    @staticmethod
    def files_path_gen(path):
        return (str(Path(p).joinpath(file)) for p, _, files in os.walk(path) for file in files)

    @staticmethod
    def dirs_path_gen(path):
        return (str(Path(p).joinpath(d)) for p, dirs, _ in os.walk(path) for d in dirs)

    @staticmethod
    def get_num_of_dirs(path):
        return sum([len(dirs) for _, dirs, _ in os.walk(path)])

    @staticmethod
    def get_num_of_files(path):
        return sum([len(files) for _, _, files in os.walk(path)])

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
            return (file for file in [self.__path])
        elif Path(self.__path).is_dir():
            return self.files_path_gen(self.__path)

    def get_dirs(self) -> iter:
        """Returns the folder path generator"""
        if Path(self.__path).is_dir():
            return self.dirs_path_gen(self.__path)
        return []

    @property
    def num_of_files(self):
        return 1 if Path(self.__path).is_file() else self.get_num_of_files(self.__path)

    @property
    def num_of_dirs(self):
        return self.get_num_of_dirs(self.__path)

    def __str__(self):
        return f'PathObj({self.__path})'


class DataObj:

    def __init__(self):
        self.__objects = {}

    def get_obj_gen(self):
        return (obj for obj in self.__objects.values())

    def get_obj_dict(self):
        return self.__objects

    def add_path(self, path: str) -> bool:
        if os.path.exists(path) and not self.search_for_duplicates(path) and not os.path.islink(path):
            self.__objects[path] = PathObj(path)
            return True
        return False

    def search_for_duplicates(self, path: str) -> bool:
        """Checking for duplicates"""
        return True if path in self.__objects else False

    def del_path(self, path: str) -> bool:
        """Deleting a path object"""
        if self.search_for_duplicates(path):
            del self.__objects[path]
            return True
        return False

    def get_files(self) -> iter:
        """Returns a generator with file paths from all objects"""
        return (file for obj in self.__objects.values() for file in obj.get_files())

    def get_dirs(self) -> iter:
        """Getting folders"""
        return reversed(sorted(path for obj in self.__objects.values() for path in obj.get_dirs()))

    @property
    def is_any_data(self) -> bool:
        """Checking for data in repositories"""
        return True if self.__objects else False

    def clear_data(self) -> None:
        """Clearing storage"""
        self.__objects.clear()
