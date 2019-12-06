
[![](https://codecov.io/gh/whoopnip/pypi-sphinx-quickstart/branch/master/graph/badge.svg)](https://codecov.io/gh/whoopnip/pypi-sphinx-quickstart)

# pypi-sphinx-quickstart

## Overview

This repo is a template to use for starting a new Python package
which is hosted on PyPi and uses Sphinx for documentation
hosted on Github pages. It has a built-in CI/CD system using Github Actions, 
all you need to do for that is hook up the secrets. The CI system has
the following features:
- Runs any tests in `tests` with `pytest`
- Lints code using `flake8`
- Static code checks with `mypy`
- Deploys PyPI package
- Deploys Sphinx documentation on Github Pages
    - Autodoc/autosummary already set up
    - Automatic sitemap.xml generated
    - Just add Google Analytics ID to enable tracking
    - Read the Docs Theme with Custom CSS
    - Notebook-style examples with Sphinx Gallery complete with download and Binder links
        - Auto-converts Jupyter notebooks in `nbexamples`
- Auto-merges pull requests by maintainers
- Auto-drafts release notes based on merged pull requests
- Collects TODO comments and converts them into issues (optional)
- Closes TODO issues once comments are removed (optional)

## Getting Started

### Required Steps

Click the "Use this template" button at the top of the repo page, then 
fill out the name and description your new repo. Once you have the repo,
make the following edits.

#### Adding Secrets

Go into the repo settings, under Secrets, and add the following secrets:
- `pypi_password`: Personal token for PyPI
- `gh_token`: Github personal access token
- `CODECOV_TOKEN` (optional): [codecov.io](https://codecov.io) token for this project  
- `TODO_ACTIONS_MONGO_URL` (optional): MongoDB connection url, complete with
username and password. See [Setup MongoDB](#setup-mongodb-optional-for-todo-integration).

#### `conf.py`

Edit `conf.py` in the main repo directory. This contains the main 
settings for the PyPi package. Fill out each setting with the 
details about your package.

#### Adding Project Source

Delete the folder `py_qs_example`, and add your own package
with the name you set in `conf.PACKAGE_NAME`. 

#### Adding Global Requirements to Build

If you do not already have `pipenv` installed, you will need to run:
```
pip install pipenv
```
Then regardless of whether you already had `pipenv` installed, you will
need to navigate to the repo folder and run:
```
pipenv update
```

#### Setting up Documentation

Edit `docsrc/Makefile` to change `SPHINXPROJ` to set it to the name
you set in `conf.PACKAGE_NAME`.

Edit `docsrc/source/index.rst` to remove the example included files. Replace
with your own if you wish or entirely delete the My Module and 
My Package sections if don't wish to use the autosummary directive.

Edit `docsrc/source/tutorial.rst` to put your own tutorial, or remove it
and remove it from the `toctree` directive in `docsrc/source/index.rst`.

You may further modify Sphinx configuration in `docsrc/source/conf.py`
if you wish.

Add [Sphinx Gallery](https://sphinx-gallery.github.io/stable/index.html) examples
in the `examples` folder. You can also add Jupyter notebook examples in the 
`nbexamples` folder, and they will automatically be converted to 
Sphinx Gallery-style examples and included with `examples` in the 
build of the documentation.

#### Commit and Push

After the preceding steps, now commit your changes and push to `master`
if not done already. After a few minutes, Github Actions should create
a `gh-pages` branch which has the documentation HTML in it.

#### Github Pages Setup

Go to repo settings, Github Pages section. For the Source dropdown, 
select "gh-pages branch". The settings page should reload,
and in the Github Pages section it should show the URL of your 
documentation. You should be able to see the documentation at the URL
after a few seconds, but it will still be the example documentation.

If "gh-pages branch" is not shown in the dropdown, you need to make one 
release commit and push it, so that the `gh-pages` branch will be added 
to your repo. After doing that, you can go into the repo settings
and select "gh-pages branch" as described.

### Optional Steps

### Adding Labels

The following labels are used in the CI/CD. They should be added in Labels in the
repo settings:
- `no auto merge`: added to prevent automatic merging of 
pull requests by maintainers
- `maintenance`: one of the output categories for release notes

### Set Master to Protected Branch

It is recommended to make master a protected branch so that nobody can
delete it. 

### Setup Codecov

Go to [codecov.io](https://codecov.io), log in via Github, click Repositories then 
"Add new repository" and select this repository from the list. Copy the
token for Codecov to use in the next step.

### Setup MongoDB (optional, for TODO integration)

For the TODO integration to work, you need a MongoDB instance. You can
get one for free at [mlab.com](https://mlab.com). After creating the database,
create a database user. The MLab interface will show you the format
of the connection url string, which you will fill in the database user's 
username and password and use that as the `TODO_ACTIONS_MONGO_URL` secret,
as the [Adding Secrets](#adding-secrets) section shows.

## Built-in CI/CD

### On Every Push

Github Actions are used to automatically run the following steps on every push:
- Check Python syntax with `flake8`
- Run `pytest`
- Static typing checks with `mypy`

### When Branch is `master`

If the branch is the `master` branch, then it will also:
- Upload `pytest` results to `codecov`

#### If there is a change in `docsrc`

If the branch is the master branch, and there was a change in `docsrc`, it will do 
all the steps in On Every Push and When Branch is `master`, then it will:
- Build documentation HTML using Sphinx
- Create `gh-pages` branch and copy HTML there
- Push to `gh-pages` branch, which will update the hosted documentation 

#### If there is a change in the package version
If the branch is the master branch, and there was a change in the package version
in `conf.py`, it will do 
all the steps in On Every Push and When Branch is `master`, then it will:
- Build documentation HTML using Sphinx
- Create `gh-pages` branch and copy HTML there
- Push to `gh-pages` branch, which will update the hosted documentation 
- Build Python package
- Upload Python package to PyPI

### If a Pull Request is Opened
The CI/CD system will check whether the pull request was opened by a maintainer
(configured in conf.py). If so, it will auto-merge the pull request after
it has passed CI checks. It will then run the deployment pipeline. To avoid
this auto-merge behavior, add the label "no auto merge" to the pull request.

## Regular Usage

Once everything is set up, just commit your changes. The built-in
CI/CD will take care of testing, build, and deployment of PyPI package
and documentation. If you use pull requests on Github then it will
show you whether it passes the CI tests.

### Releases

If you want to create Github releases notes for your package, they
will already be drafted, just edit them as desired before posting.

## Local Usage

Building the documentation locally makes sense if you are
updating it but don't want to make it live yet. You can view
the HTML files in the `docs` folder via a browser after building them.

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

## Links

See the example 
[generated documentation here.](
https://whoopnip.github.io/pypi-sphinx-quickstart/
)
