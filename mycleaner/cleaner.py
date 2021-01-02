#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -----------------------------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details)
# Copyright © 2020-2021 Aleksandr Suvorov
# -----------------------------------------------------------------------------
"""Module for destruction, zeroing, and deleting files.

Used to create applications for destruction, zeroing, and deleting files.
Delete a folder. After being reset or destroyed, file recovery is impossible or
extremely difficult.

To destroy it, use the utility shred.
"""
import os
import shlex


class Cleaner:
    """Creates an object for working with file and folder paths

    for further destruction, zeroing, deleting files. Delete a folder.
    """
    def __init__(self, root=False, shreds=30):
        """Accepts an optional parameter when creating an object shred:

        the number of passes to overwrite the file. By default, 30 passes.
        """
        self.errors = []
        self.root = root
        # Number of passes to overwrite the file
        self.shreds = shreds

        # Counters
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    @staticmethod
    def replace_path(path: str) -> str:
        return shlex.quote(path)

    @staticmethod
    def check_exist(path):
        if os.path.exists(path):
            return True
        return False

    def zero_file(self, file: str) -> bool:
        """Resets the file to the specified path"""
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            self.errors.append(f'Zeroing error: {file}')
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, path: str) -> bool:
        """Overwrites and deletes the file at the specified path"""
        rep_path = self.replace_path(path)
        if os.name == 'posix':
            if self.root:
                os.system(f'sudo shred -zvuf -n {self.shreds} {rep_path}')
            else:
                os.system(f'shred -zvu -n {self.shreds} {rep_path}')
        else:
            self.del_file(path)
        if self.check_exist(path):
            self.errors.append(f'Do not shred: {path}')
            return False
        else:
            self.count_del_files += 1
            return True

    def del_file(self, path: str) -> bool:
        """Deletes the file at the specified path using normal deletion"""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                self.zero_file(path)
                os.remove(path)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        if self.check_exist(path):
            self.errors.append(f'Do not delete: {path}')
            return False
        else:
            self.count_del_files += 1
            return True

    def del_dir(self, path: str) -> bool:
        """Deletes an empty folder at the specified path"""
        try:
            if os.path.islink(path):
                os.unlink(path)
            else:
                os.rmdir(path)
        except OSError:
            self.errors.append(f'Os error! Do not delete: {path}')
            return False
        else:
            if self.check_exist(path):
                self.errors.append(f'Do not delete: {path}')
                return False
            else:
                self.count_del_dirs += 1
                return True

    def reset_count(self) -> None:
        """Resetting counters"""
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    def reset_error_list(self):
        self.errors.clear()
