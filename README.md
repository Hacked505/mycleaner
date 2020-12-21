My cleaner
===

    A package of modules and console utilities for destroying,
    zeroing, and deleting files.

>Created: Aleksandr Suvorov

![GitHub repo size](https://img.shields.io/github/repo-size/mysmarthub/mycleaner)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/mycleaner?label=pypi%20downloads)](https://pypi.org/project/mycleaner/)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/mycleaner/total?label=github%20downloads)](https://github.com/mysmarthub/mycleaner/)
![GitHub](https://img.shields.io/github/license/mysmarthub/mycleaner)
![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/mycleaner?style=social)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)
[![PyPI](https://img.shields.io/pypi/v/mycleaner)](https://pypi.org/project/mycleaner/)
![PyPI - Format](https://img.shields.io/pypi/format/mycleaner)

---
[![Download mycleaner](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
[![Download mycleaner](https://img.shields.io/sourceforge/dt/mycleaner-package.svg)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

Help the project financially:
---
>Yandex Money:
https://yoomoney.ru/to/4100115206129186

    Visa:    4048 4150 0400 5852

    Sberbank Russia: 4276 4417 5763 7686

https://paypal.me/myhackband

---

Description:
---
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

---
Help:
---
```
usage: Smart Files Destroyer [-h] [--log] [--version] paths [paths ...]

Console utilities for destroying, zeroing, and deleting files

positional arguments:
  paths       Paths to files and folders

optional arguments:
  -h, --help  show this help message and exit
  --log       Save errors log
  --version   Program version

https://githib.com/mysmarthub/sfd

```

>Package installation:

`pip install mycleaner`

>Git Clone:

`git clone https://github.com/mysmarthub/mycleaner/`

---

>Use:

```python
# Import the cleaner module to create the object
# Import the smart module to create an object for storing and working with 
# paths or create your own objects

# from mycleaner import cleaner, smart
```
>To run the utility, use:

```
python sfd.py '/path' --log
```


>After entering the command, you can enter the necessary folders or files
, or simply drag them to the console. Their absolute paths will be used after launch.

---
>Additionally:

>After installing the package, you can run the utility by calling the command:
>Be careful! When adding folders, all files from all subfolders 
will be added recursively.

    After installing the package with the command pip install mycleaner,
    you can run the console utility with the following command:

>Running in the console:

```
mycleaner '/path' --log
```

```
python sfd.py '/path' --log
```

---

>To delete some files, you may need administrator rights .
> To do this, install the package with the command:

```
sudo pip install mycleaner
```

```
sudo mycleaner '/path' --log
```

```commandline
sudo python sfd.py '/path' --log
```

---
Links:
---
>[GitHub](https://github.com/mysmarthub/mycleaner)

>[PyPi](https://pypi.org/project/mycleaner/)
 
>[Sourceforge](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

Disclaimer of liability:
------------------------
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

Support:
---
    Email: myhackband@yandex.ru
    Copyright © 2020 Aleksandr Suvorov
