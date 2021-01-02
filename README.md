My cleaner
===

>A package of modules and console utilities for destroying, 
> zeroing, and deleting files.

>Developer: Aleksandr Suvorov

>BSD 3-Clause License 

[![PyPI - Downloads](https://img.shields.io/pypi/dm/mycleaner?label=pypi%20downloads)](https://pypi.org/project/mycleaner/)
[![PyPI](https://img.shields.io/pypi/v/mycleaner)](https://pypi.org/project/mycleaner/)
[![PyPI - Format](https://img.shields.io/pypi/format/mycleaner)](https://pypi.org/project/mycleaner/)
[![GitHub repo size](https://img.shields.io/github/repo-size/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)
[![GitHub all releases](https://img.shields.io/github/downloads/mysmarthub/mycleaner/total?label=github%20downloads)](https://github.com/mysmarthub/mycleaner/)
[![GitHub](https://img.shields.io/github/license/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)
[![GitHub Repo stars](https://img.shields.io/github/stars/mysmarthub/mycleaner?style=social)](https://github.com/mysmarthub/mycleaner)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/mysmarthub/mycleaner)](https://github.com/mysmarthub/mycleaner/)


---
[![Download mycleaner](https://a.fsdn.com/con/app/sf-download-button)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
[![Download mycleaner](https://img.shields.io/sourceforge/dt/mycleaner-package.svg)](https://sourceforge.net/projects/mycleaner-package/files/latest/download)
---

![Mycleaner](https://github.com/mysmarthub/mycleaner/raw/master/images/my_cleaner_logo.png)

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
>A package of modules and console utilities for destroying, 
> zeroing, and deleting files.

>With this package, you can develop graphical, 
> console , and cross-platform applications to destroy, 
> reset data in a file, and delete files 
> so that they are difficult or impossible to recover. 
> 
>You can also use a ready-made console utility for destruction, 
> reset and delete files, as well as use the graphical utility 
> developed using the mycleaner and pyside2 package.
> 
>Console utility for destruction,
> zeroing, and deleting files.
>
>The utility allows you to destruct files, 
> reset them to zero and delete them, 
> for complete or partial difficulty in 
> restoring them after deletion.
> 
> >Be careful! When adding folders, all files from all subfolders 
will be added recursively.
> 
> >When you run the program with all the parameters, 
> all files located at the specified path will be destroyed, 
> including those nested in other folders,
> if you specify all the arguments, then after 
> starting the utility will start working without 
> confirmation, so be very careful!
> 
> The utility can be run with or without command 
> line arguments to allow you to select the desired parameters manually.
> 
> Run the utility without arguments and follow the instructions below.
> 
> To run the utility with arguments, 
> if you specify all the arguments, then after 
> starting the utility will start working without confirmation, 
> so be very careful! If you do not specify 
> one of the important arguments such as the path, 
> the number of mashing or the method to work with, 
> the utility will start, but will prompt you to enter 
> the necessary parameters.


---
Help:
---
```
usage: My Cleaner [-h] [--p P [P ...]] [--o O] [--s] [--z] [--d] [--log]
                  [--version]

Smart Console utility for destroying (shred), zeroing, and deleting files

optional arguments:
  -h, --help            show this help message and exit
  --p P [P ...], --paths P [P ...]
                        Paths to files and folders
  --o O, --overwrites O
                        Number of overwrites
  --s                   Shredding and delete file
  --z                   Zeroing no delete file
  --d                   Zeroing and delete file
  --log                 Save errors log
  --version             Program version

```

>Package installation:

`pip install mycleaner`

>Git Clone:

`git clone https://github.com/mysmarthub/mycleaner`

---

>Use:

`mycleaner --p /path/ /path2/file.file --o 100 --s --log`

>To delete some files, you may need administrator rights. 
> To do this, install the package with the command:
> 
>`sudo pip install mycleaner`
> 
>`sudo mycleaner --p /path/ /path2/file.file --o 100 --s --log`

>To run the utility, use:

```
git clone https://github.com/mysmarthub/mycleaner.git
cd mycleaner
pip install -r requirements
python mycleaner/mycleaner.py --p /path/ /path2/file.file --o 100 --s --log
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
    Copyright © 2020-2021 Aleksandr Suvorov
