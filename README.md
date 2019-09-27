# cyrtd

## Description 

Here we will go through all the steps to make Cython package, 
Sphinx auto documentation and poetry work together. I will 
write about my experience, so this is not a tutorial, but
something, that may be useful for you


## Project skeleton

First of all new public repository on github was created.
In my case it was called `cyrtd`, so please replace this name
to yours if you want to replicate the results. 

### Poetry

For the next step you will need [poetry](https://github.com/sdispater/poetry)

```bash
poetry new cyrtd
cd cyrtd
git init
git remote add origin <repo>
git pull <repo> master
git add *
git commit -m <message>
git push --set-upstream origin master
```

I also deleted `README.rst` and `test` folder to makes things easy.

The next step will be related to documentation

### Virtual environment

Some time ago I discovered [pipenv](https://github.com/pypa/pipenv)
and found it very useful. So now I have only Python3 installed on my machine and all the packages
needed for my projects are installed inside virtual envs related to this
projects.

```bash
pipenv install
pipenv shell
```


### Sphinx

Install [Sphinx](https://docs.readthedocs.io/en/stable/intro/getting-started-with-sphinx.html)
and move to the creation of `docs` folder with necessary  stuff:

```bash
mkdir docs
cd docs
pipenv run sphinx-quickstart
```

[Guide](https://sphinx-rtd-tutorial.readthedocs.io/en/latest/sphinx-quickstart.html)
to quicksart.

Finally I have this state:
```
│   .gitignore
│   Pipfile
│   Pipfile.lock
│   pyproject.toml
│   README.md
│
├───cyrtd
│       __init__.py
│
└───docs
    │   make.bat
    │   Makefile
    │
    ├───build
    └───source
        │   conf.py
        │   index.rst
        │
        ├───_static
        └───_templates
```

## Writing source

For gentle diving into the field, firstly we will create clear pythonic
package. This is what we added:

```bash
│───cyrtd
│   │   __init__.py
│   │
│   └───pymod
│           pyfuncs.py
│           __init__.py
```

In `pyfuncs.py`:
```python
from typing import Union


def square(num: Union[int, float]):
    """
    Function squares the input

    Parameters
    ----------
    num: int, float

    Returns
    -------
    int, float
        Squared argument
    """
    return num**2
```
I prefer NumPy style documentation, so here we are.

## Spinx settings

Probably the most important file, related to sphinx, is `conf.py`. A couple
of important things.

First of all, if your documentation is in separate folder you have
to make sphinx be able to import your package:

```python
import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
```

Add several extensions:

```python
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx'
]
```

`autodoc` for making documentation automatically, `napoleon` for sphinx
to be able to fetch NumPy-style documentation, `intersphinx` for being
able to reference other projects' documentation.

It is also important to add to point sphinx at main `.rst` document
`index.rst` in my case
```python
master_doc = 'index'
```

The next step is to add logic to thee way we want to display the
documentation. So it's time for `.rst` files. 

In my opinion each logical part should be described in separate `.rst`
file. So let's create `api.rst` next to `index.rst` with following
content:

```
.. _api:

API Reference
=============

Py functons
-----------

.. automodule:: cyrtd.pymod.pyfuncs
	:members:
	:inherited-members:
```

`index.rst`:
```
Cython package docs
===================

.. toctree::
   :maxdepth: 2

   api.rst
```

Seems like we are ready to build documentation locally. From `docs/`
run:

```bash
make html
```

Initially it does not look fancy, but still you can open it with 
you browser from `docs/build`

Commit your changes and let's host our docs online.

## Read the Docs

[How to import](https://docs.readthedocs.io/en/stable/intro/import-guide.html)

