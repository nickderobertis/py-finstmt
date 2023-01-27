

[![](https://codecov.io/gh/nickderobertis/py-finstmt/branch/master/graph/badge.svg)](https://codecov.io/gh/nickderobertis/py-finstmt)
[![PyPI](https://img.shields.io/pypi/v/finstmt)](https://pypi.org/project/finstmt/)
![PyPI - License](https://img.shields.io/pypi/l/finstmt)
[![Documentation](https://img.shields.io/badge/documentation-pass-green)](https://nickderobertis.github.io/py-finstmt/)
![Tests Run on Ubuntu Python Versions](https://img.shields.io/badge/Tests%20Ubuntu%2FPython-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Macos Python Versions](https://img.shields.io/badge/Tests%20Macos%2FPython-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Windows Python Versions](https://img.shields.io/badge/Tests%20Windows%2FPython-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)
[![Github Repo](https://img.shields.io/badge/repo-github-informational)](https://github.com/nickderobertis/py-finstmt/)


#  py-finstmt

## Overview

Contains classes to work with financial statement data. Can calculate free cash flows and help project financial statements.

## Getting Started

Install `finstmt`:

```
pip install finstmt
```

A simple example:

```python
import finstmt

# Do something with finstmt
```

See a
[more in-depth tutorial here.](
https://nickderobertis.github.io/py-finstmt/tutorial.html
)

## Development Status

This project is currently in early-stage development. There may be
breaking changes often. While the major version is 0, minor version
upgrades will often have breaking changes.

## Developing

First, you need a couple global dependencies installed, see their documentation for details:
- [direnv](https://direnv.net/docs/installation.html)
- [asdf](https://asdf-vm.com/guide/getting-started.html)

Note that these tools require a UNIX-style shell, such as bash or zsh. If
you are on Windows, you can use WSL or Git Bash. If you are using Pycharm,
you can configure the built-in terminal to use Git Bash.

Then clone the repo and run `direnv allow`. This will take a while on the first time
to install the remaining dependencies.

Make your changes and then run `just` to run formatting,
linting, and tests.

Develop documentation by running `just docs` to start up a dev server.

To run tests only, run `just test`. You can pass additional arguments to pytest,
e.g. `just test -k test_something`.

Prior to committing, you can run `just` with no arguments to run all the checks.

## Author

Created by Nick DeRobertis. MIT License.

## Links

See the
[documentation here.](
https://nickderobertis.github.io/py-finstmt/
)

## Author

Created by Nick DeRobertis. MIT License.