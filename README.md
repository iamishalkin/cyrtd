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