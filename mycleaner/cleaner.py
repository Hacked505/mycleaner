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
from random import randint


class Cleaner:
    def __init__(self, shreds=30):
        self.shreds = shreds
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0

    @staticmethod
    def replace_path(path: str) -> str:
        symbol = ' !$^&*()=|[]{}?,<>"\':`;'
        for s in symbol:
            if s in path:
                path = path.replace(s, f'\\{s}')
        return path

    def zero_file(self, file: str) -> bool:
        try:
            with open(file, 'wb') as f:
                f.write(bytes(0))
        except OSError:
            return False
        else:
            self.count_zero_files += 1
            return True

    def shred_file(self, path: str) -> bool:
        if os.name == 'posix':
            file = self.replace_path(path)
            os.system(f'shred -zvu -n {self.shreds} {file}')
        else:
            try:
                for i in range(self.shreds):
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
        self.count_zero_files = 0
        self.count_del_files = 0
        self.count_del_dirs = 0
