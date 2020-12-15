"""A package of modules and console utilities for destroying, zeroing, and deleting files

mycleaner
===============

    A package of modules and console utilities for destroying,
    zeroing, and deleting files.
    -------------------------------------------------------
    With this package, you can develop graphical,
    console , and cross-platform applications to destroy,
    reset data in a file, and delete files
    so that they are difficult or impossible to recover.
    -------------------------------------------------------
    You can also use a ready-made console utility for destruction,
    reset and delete files, as well as use the graphical utility
    developed using the mycleaner and pyside2 package.

mycleaner [github.com](http://github.com/mysmarthub/mycleaner/)

mycleaner [pypi.org](http://github.com/mysmarthub/mycleaner/)

[Smart Cleaner](http://github.com/mysmarthub/smartcleaner/)

Launch and use:
---------------


Package installation:
---------------------

pip install mycleaner

Git Clone:

git clone https://github.com/mysmarthub/mycleaner/

---

Use:
----

# Import the cleaner module to create the object
# Import the smart module to create an object for storing and working with
# paths or create your own objects
from mycleaner import cleaner, smart
my_cleaner = cleaner.Cleaner(shreds=30)
my_data_path = smart.DataObj()

To run the utility, use:

python term_my_cleaner.py path to the file / files folder/folders with files

After entering the command, you can enter the necessary folders or files
, or simply drag them to the console. Their absolute paths will be used after launch.

---

Additionally:
-------------
After installing the package, you can run the utility by calling the command:
Be careful! When adding folders, all files from all subfolders
will be added recursively.

    After installing the package with the command pip install mycleaner,
    you can run the console utility with the following command:

Running in the console:
-----------------------

myclenaer [/path/<file>|<dir>]

---

To delete some files, you may need administrator rights
. to do this, install the package with the command:

sudo pip install mycleaner

sudo mycleaner [paths]

sudo python term_my_cleaner.py [paths]


Support:
========
    Author: Aleksandr Suvorov
    Email: myhackband@yandex.ru

GitHub: https://github.com/mysmarthub/mycleaner

PyPi: https://pypi.org/project/mycleaner/

Help the project financially:
-----------------------------
Yandex Money:

https://money.yandex.ru/to/4100110928527458

Sberbank Russia:

4276 4417 5763 7686

"""
__version__ = '1.1.6'
__author__ = 'Aleksandr Suvorov'
