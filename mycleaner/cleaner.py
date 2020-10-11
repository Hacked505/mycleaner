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
"""Module for destroying, zeroing and deleting files

Classes:
--------

Cleaner

    Methods:
    -------
    zero_file(self, file: str) -> bool:
    shred_file(self, path: str, shreds: int) -> bool:
    del_file(self, path: str) -> bool:
    del_dir(self, path: str) -> bool:
    reset_count(self) -> None:

    @staticmethod
    replace_path(path: str) -> str:
"""
import os
from random import randint


class Cleaner:
    """Mashing, zeroing, and deleting files

    Attributes:
        self.count_zero_files:int - Counter for zeroed files
        self.count_del_files:int - Deleted file counter
        self.count_del_dirs:int - Deleted folder counter

    Methods:
        replace_path(path: str) -> str: - linux path escaping
        zero_file(self, file: str) -> bool: - resets the file
        shred_file(self, path: str, shreds: int) -> bool: - overwrites the file
        del_file(self, path: str) -> bool: - deletes the file
        del_dir(self, path: str) -> bool: - deletes a folder
        reset_count(self) -> None: - resetting counters

    """

    def __init__(self):
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    @staticmethod
    def replace_path(path: str) -> str:
        """Linux path escaping

        Parameters:
            path - path to the file or folder

        Returns:
            path: str - If forbidden characters are found in the path,
            returns the corrected path, if not, the original path
        """
        symbol = ' !$^&*()=|[]{}?,<>"\':`;'
        for s in symbol:
            if s in path:
                path = path.replace(s, f'\\{s}')
        return path

    def zero_file(self, file: str) -> bool:
        """Resets the file

        Parameters:
            file: str - path to the file

        Returns:
            True/False: bool - return the logical result of zeroing the file
        """

        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, path: str, shreds: int) -> bool:
        """Overwrites the file with random data and deletes it

        Parameters:
            path: str - path to the file
            shreds: int - number of passes/rewrites

        Returns:
            True/False: bool - Returns the logical status of file overwriting.
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
        """Deletes the file in the usual way

        Parameters:
            path: str - path to the file

        Returns:
            True/False: bool -returns the logical status of deleting a file
        """
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
        """Deletes a folder

        Parameters:
            path: str - path to the folder

        Returns:
            True/False: bool -returns the logical status of deleting a folder
        """
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
        """Resets counters"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0


def main():
    pass


if __name__ == '__main__':
    main()
