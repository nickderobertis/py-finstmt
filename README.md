

[![](https://codecov.io/gh/nickderobertis/py-finstmt/branch/master/graph/badge.svg)](https://codecov.io/gh/nickderobertis/py-finstmt)
[![PyPI](https://img.shields.io/pypi/v/finstmt)](https://pypi.org/project/finstmt/)
![PyPI - License](https://img.shields.io/pypi/l/finstmt)
[![Documentation](https://img.shields.io/badge/documentation-pass-green)](https://nickderobertis.github.io/py-finstmt/)
![Tests Run on Ubuntu Python Versions](https://img.shields.io/badge/Tests%20Ubuntu%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Macos Python Versions](https://img.shields.io/badge/Tests%20Macos%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
![Tests Run on Windows Python Versions](https://img.shields.io/badge/Tests%20Windows%2FPython-3.8%20%7C%203.9%20%7C%203.10-blue)
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
from finstmt import BalanceSheets, IncomeStatements, FinancialStatements
import pandas as pd

bs_path = r'WMT Balance Sheet.xlsx'
inc_path = r'WMT Income Statement.xlsx'
bs_df = pd.read_excel(bs_path)
inc_df = pd.read_excel(inc_path)
bs_data = BalanceSheets.from_df(bs_df)
inc_data = IncomeStatements.from_df(inc_df)
stmts = FinancialStatements(inc_data, bs_data)
```

See a
[more in-depth tutorial here.](
https://nickderobertis.github.io/py-finstmt/tutorial.html
)

## Links

See the
[documentation here.](
https://nickderobertis.github.io/py-finstmt/
)

## Development Status

This project is currently in early-stage development. There may be
breaking changes often. While the major version is 0, minor version
upgrades will often have breaking changes.

## Developing

See the [development guide](
https://github.com/nickderobertis/py-finstmt/blob/master/DEVELOPING.md
) for development details.

## Author

Created by Nick DeRobertis. MIT License.

