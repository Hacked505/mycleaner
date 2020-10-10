"""A package of modules for overwriting, zeroing, and deleting files.

With this package, you can develop graphical,
console, and cross-platform applications for destroying,
zeroing, and deleting files to make
it difficult or impossible to restore them.

Modules:
--------

smart
cleaner

Info:
------

smart - Add, temporarily store, delete, and get paths to files and
folders for further work with them. The path will be used for the
destruction/deletion of files/folders.

  You can use instances of the MyPath class to store paths to deleted files/folders,
  or deliver the paths yourself.

    add_path(self, path: str) -> bool:
    del_path(self, path: str) -> bool:

    get_files(self) -> iter:
    get_folders(self) -> iter:

    search_for_duplicates(self, path: str) -> bool:
    clear_data(self) -> None:

    @property
    is_any_data(self) -> bool:


cleaner - Mashing, zeroing, deleting files. Delete a folder.
To destroy a file in Linux use the shred utility.

You can use instances of the MyPath class to store paths
to deleted files/folders, or deliver the paths yourself.

    replace_path(path: str) -> str:
    zero_file(self, file: str) -> bool:
    shred_file(self, path: str, shreds: int) -> bool:
    del_file(self, path: str) -> bool:
    del_dir(self, path: str) -> bool:
    reset_count(self) -> None:

"""
__version__ = '1.0.9'
__author__ = 'Aleksandr Suvorov'
