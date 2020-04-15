from dataclasses import dataclass
from typing import Dict

import pandas as pd

from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.inc.data import IncomeStatementData


@dataclass
class IncomeStatements(FinStatementsBase):
    """
    Main class for holding income statement data. Usual way to construct is with the .from_df method.

    Examples:
        >>> inc_path = r'WMT Income Statement.xlsx'
        >>> inc_df = pd.read_excel(inc_path)
        >>> inc_data = IncomeStatements.from_df(inc_df)
    """
    statements: Dict[pd.Timestamp, IncomeStatementData]  # type: ignore

    statement_cls = IncomeStatementData  # type: ignore
    statement_name = 'Income Statement'
