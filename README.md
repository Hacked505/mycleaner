My Cleaner (mycleaner)
===
A package of modules for zeroing, destroying,
and deleting files. Delete folders,
as well as to work with paths to files and folders.

With this package, you can develop programs to reset, erase,
and delete files.
Graphical, console, cross-platform, without worrying about
methods for deleting, zeroing, and mashing.
Store data in Smart objects and use the Cleaner object for cleaning.

Example of using the Smart Cleaner program.
http://www.hackband.ru

Install: 
---
`pip install mycleaner`

`pip3 install mycleaner`

Use: from mycleaner.cleaner import Smart, Cleaner

>Smart() - Storage, addition, extraction, counting,
removal of paths to files and folders. When adding a folder,
all the data attached to it is taken into account and added recursively.

    smart = Smart()

    smart.add_path(self, path: str) -> bool:  - adds a new path to a file or folder.
    Returns the logical status of adding a path to a file or folder.

    smart.del_path(self, path: str) -> bool: - deletes the path.
    Returns the logical status of deleting the path
    to a file or folder. Removes a path from the repository.

    get_files_gen(self) -> iter: - Returns a generator containing paths to all files.
    Including files attached to folders, objects that were added to the storage.

    def get_folders_gen(self) -> iter: - Returns an iterator containing paths to all files.
    Including files attached to folders, objects that were added to the storage.

    @property
    def is_any_data(self) -> bool: - Returns the logical status of checking for the presence
    absence of added paths.

    def search_for_duplicates(self, path: str) -> bool: - Returns the logical
    status of the duplicate path check.

    def clear_data(self) -> None: - Cleans storage with paths

>Cleaner() - Mashing, zeroing, and deleting files/folders.
When using methods of this class, be very careful, as the data will be destroyed.

    self.count_zero_files - reset file counter
    self.count_del_files - counter for deleted files
    self.count_del_dirs - counter for deleted folders

        @staticmethod
        def replace_path(path: str) -> str: - Linux path escaping.
        Solves the problem with paths in Linux.

        def zero_file(self, file: str) -> bool: - Resets the file. Return The logical result of
        zeroing the file.

        def shred_file(self, path: str, shreds: int) -> bool: - Overwrites the file
        with random data and deletes it. Returns the logical status of file overwriting.

        def del_file(self, path: str) -> bool: - Deletes the file in the usual way, returns status.

        def del_dir(self, path): - Deletes a folder, returns status.

        def reset_count(self) -> None: - Resets counters to 0.

>MyFolder() - Auxiliary class for Smart().
Folder object. When creating an instance, it requires an existing folder path address.
Stores the path address, allows you to get recursively.

    def get_files(self) -> iter: - Returns a generator containing paths to all nested files.

    def get_folders(self) -> iter: - Returns a generator containing paths to all nested folders.

    @property
    def path(self) -> str: - Returns the path to the folder whose data is stored in the object.

**Author: Aleksander Suvorov**
---

Support: myhackband@yandex.ru

Website: https://www.hackband.ru

GitHub: https://github.com/mysmarthub/mycleaner

PyPi: https://pypi.org/project/mycleaner/

Help the project financially:
---
Yandex Money: https://money.yandex.ru/to/4100110928527458

Sberbank Russia: `4276 4417 5763 7686`
