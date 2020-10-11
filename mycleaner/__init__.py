"""A package of modules for overwriting, zeroing, and deleting files.

With this package, you can develop graphical,
console, and cross-platform applications for destroying,
zeroing, and deleting files to make
it difficult or impossible to restore them.

Modules:
--------
    smart
    cleaner

smart - Module for working with file and folder paths
cleaner - Module for destroying, zeroing and deleting files

smart
=====
    Classes:
    --------
        Folder - Used for storing the path to a folder
            Methods:
                get_files(self) -> iter:
                get_folders(self) -> iter:
                @property
                path(self) -> str:

        PathData - Working with file and folder paths
            add_path(self, path: str) -> bool:
            del_path(self, path: str) -> bool:
            get_files(self) -> iter:
            get_folders(self) -> iter:
            search_for_duplicates(self, path: str) -> bool:
            clear_data(self) -> None:

            @property
            is_any_data(self) -> bool:


cleaner
=======
    Classes:
    --------
        Cleaner - Mashing, zeroing, and deleting files
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

Use:
====
Use it smart.PathData to create instances, temporarily store, add, delete,
and get paths to files and folders.

We use it cleaner.Cleaner to create instances, erase/overwrite, reset, delete files.
Delete a folder.

"""
__version__ = '1.0.9'
__author__ = 'Aleksandr Suvorov'
