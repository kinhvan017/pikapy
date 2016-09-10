# pikapy
python client for pikab.in


Installation
------------

If you have downloaded the source distribution, to install do the following at the commandline:

```
$ python setup.py install
```

Usage Examples
--------------

```
>>> from pikapy import PikaClient
>>> x = PikaClient('https://pikab.in/')
>>> url = x.paste('String ABC' ,
...               paste_title="demo paste",
...               paste_expire_after = '10m',
...               paste_syntax = 'python')
>>> print url
https://pikab.in/d91a0bf2e0979ca8648262da4ebbfdc357a79s
```
