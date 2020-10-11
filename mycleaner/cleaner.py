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


class Cleaner:
    """Mashing, zeroing, and deleting files."""

    def __init__(self):
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

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
        """Resets counters to 0

        """
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0


def main():
    pass


if __name__ == '__main__':
    main()
