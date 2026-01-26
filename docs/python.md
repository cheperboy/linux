# Python

* [color log](https://medium.com/@galea/python-logging-example-with-color-formatting-file-handlers-6ee21d363184)
 
## Import beyond top level package

``` python
import sys
from os.path import abspath as abspath
from os.path import dirname as dirname
from os.path import basename as basename
from os.path import join    as join

module_path  = abspath(dirname(__file__)) # /home/pi/Dev/home_alarm/src/nox_alarm
src_path     = dirname(module_path)       # /home/pi/Dev/home_alarm/src
sys.path.append(src_path)
```

## args, kwargs

``` python
def print_all_args(*args, **kwargs):
    for arg in args:
        print (arg)
    for key, value in kwargs.items():
        print (key, value)

def wrapper(*args):
    print_a_and_b(*args)
    
def print_a_and_b(a, b):
    print (a, b)

wrapper(1, 2)
# => 1 2

some_dict = {'val1':4, 'val2':8}
print_all_args(1, 2, foo='bar', toto='titi', *some_dict)
# => 
# 1
# 2
# val1
# val2
# foo bar
# toto titi
```

## SQLAlchemy

* [filters (like, or, in, ...)](http://www.leeladharan.com/sqlalchemy-query-with-or-and-like-common-filters)


## Path

``` python
{!python_path.py!}
```
``` python
{!../scripts/python_path.py!}
```

``` title="python_path.py"
--8<-- "python_path.py"
```


