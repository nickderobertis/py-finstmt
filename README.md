# pypi-sphinx-quickstart

## Overview

This repo is a template to use for starting a new Python package
which is hosted on PyPi and uses Sphinx for documentation
hosted on Github pages.

## Getting Started

Click the "Use this template" button at the top of the repo page, then 
fill out the name and description your new repo. Once you have the repo,
make the following edits.

### Github Pages Setup

Go to repo settings, Github Pages section. For the Source dropdown, 
select "master branch /docs folder". The settings page should reload,
and in the Github Pages section it should show the URL of your 
documentation. You should be able to see the documentation at the URL
after a few seconds, but it will still be the example documentation.

### `conf.py`

Edit `conf.py` in the main repo directory. This contains the main 
settings for the PyPi package. Fill out each setting with the 
details about your package.

### Adding Project Source

Delete the folder `py_qs_example`, and add your own package
with the name you set in `conf.PACKAGE_NAME`. 

### Adding Global Requirements to Build

If you do not already have `pipenv` installed, you will need to run:
```
pip install pipenv
```
Then regardless of whether you already had `pipenv` installed, you will
need to navigate to the repo folder and run:
```
pipenv install
```

### Setting up Documentation

Edit `docsrc/Makefile` to change `SPHINXPROJ` to set it to the name
you set in `conf.PACKAGE_NAME`.

Edit `docsrc/source/index.rst` to remove the example included files. Replace
with your own if you wish or entirely delete the My Module and 
My Package sections if don't wish to use the autosummary directive.

Edit `docsrc/source/tutorial.rst` to put your own tutorial, or remove it
and remove it from the `toctree` directive in `docsrc/source/index.rst`.

You may further modify Sphinx configuration in `docsrc/source/conf.py`
if you wish.

### Building Documentation

Navigate into the `docsrc` folder and run:
```
pipenv run make github
```

This should generate documentation HTML in the `docs` folder.

### Uploading to PyPi

Navigate to the repo base folder and run:
```
pipenv run python upload.py
```

## Regular Usage

Once everything is set up, just commit your changes, then follow the
instructions in [Building Documentation](#building-documentation) and
[Uploading to PyPi](#uploading-to-pypi).


## Links

See the example 
[generated documentation here.](
https://whoopnip.github.io/pypi-sphinx-quickstart/
)
