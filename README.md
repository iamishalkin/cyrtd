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

## Sphinx settings

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

This step is not so difficult but rather important. The docs may be found
[here](https://dxfeed-cyrtd.readthedocs-hosted.com/)

## Prettify

Now let's make your RtD looks like RtD. Just follow the 
[tutorial](https://sphinx-rtd-theme.readthedocs.io/en/latest/installing.html)

## Cython part

Now let's move to the Cython part. First of all, next to the `pymod` 
folder we create `cymod` folder with similar contents, but written in
Cython.

To compile Cython files during the installation with poetry `build.py`
should be created.

 ```python
from setuptools import Extension
from Cython.Build import cythonize

cyfuncs_ext = Extension(name='cyrtd.cymod.cyfuncs',
                        sources=['cyrtd/cymod/cyfuncs.pyx'])

EXTENSIONS = [cyfuncs_ext]


def build(setup_kwargs):
    setup_kwargs.update({
        'ext_modules': cythonize(EXTENSIONS, language_level=3),
        'zip_safe': False})
```

**Read the Docs configuration:** you have to put a tick into "Install Project"
in the "Advanced" section of your project section.

**pyproject.toml modifications:**

- Add `build = 'build.py'` into `[tool.poetry]` section
- Into `[tool.poetry.dependencies]` section add:
```
cython = "^0.29.13"
sphinx = { version = "^2.2", optional = true }
sphinx_rtd_theme = { version = "^0.4.3", optional = true  }


[tool.poetry.extras]
docs = ["sphinx", "sphinx_rtd_theme"]
```

**Sphinx modifications:** To display Cython functions we need to add new 
module to our `.rst` files. In our case you just need to add following
strings to `api.rst`:
```
Cy functions
------------

.. automodule:: cyrtd.cymod.cyfuncs
	:members:
	:inherited-members:
```

**.readthedocs.yml** For RtD you need to specify `pip` installation
method and other settings.

```
version: 2

python:
  install:
    - method: pip
      path: .
      extra_requirements:
        - docs

sphinx:
  configuration: docs/source/conf.py
``` 

As we point at the path here the following lines of code should be 
commented in `conf.py`:

```python
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../..'))
```

According to the documentation and discussions on github issues this
should be enough.

**However!** This did not work for me completely. On RtD side I always
got the error related to the absence of `setup.py`. I did not find the
better way to solve this issue than to write wrapper over `build.py` in
`setup.py`. So here we are:

```python
from distutils.core import setup
from build import *

global setup_kwargs

setup_kwargs = {}

build(setup_kwargs)
setup(**setup_kwargs)
```

Some people also face an issue with cached virtual envs. It is
recommended to go to "Versions" section in you RtD dashboard and wipe the 
environments. 

## Finally

We have combined Cython, ReadtheDocs and Spinx. The result may be seen
[here](https://dxfeed-cyrtd.readthedocs-hosted.com/en/latest/index.html).
This step-by-step tutorial was made as there was no anything similar and I
hope, this should be useful for someone.

All the comments about workaround over `setup.py` will be appreciated.

The final project structure:
```
│   .gitignore
│   .readthedocs.yml
│   build.py
│   pyproject.toml
│   README.md
│   setup.py
│
├───cyrtd
│   │   __init__.py
│   │
│   ├───cymod
│   │       cyfuncs.pyx
│   │       __init__.py
│   │
│   └───pymod
│           pyfuncs.py
│           __init__.py
│
└───docs
    │   make.bat
    │   Makefile
    │
    └───source
        │   api.rst
        │   conf.py
        │   index.rst
        │
        ├───_static
        └───_templates
```
