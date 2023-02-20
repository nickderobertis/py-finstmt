import re
from typing import Final, Sequence

import prettyprinter

from finstmt import FinancialStatements

always_exclude: Final[Sequence[str]] = ("_combinator",)


def format_statement_for_snapshot(
    stmts: FinancialStatements, exclude: Sequence[str] = tuple()
) -> str:
    rounded = round(stmts / 1000)
    formatted_str = prettyprinter.pformat(rounded)
    # TODO: Better support for setting values in finstmt
    #  This is a hacky way to exclude attributes. If we could copy statements setting new values,
    #  we could zero out the values we don't want to snapshot.
    for attr in (*always_exclude, *exclude):
        # Match the attribute name, equals, and everything until the end of the line
        pattern = re.compile(rf"\s*{attr}=.*$", re.MULTILINE)
        formatted_str = pattern.sub("", formatted_str)
    return formatted_str
