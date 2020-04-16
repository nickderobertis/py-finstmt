from dataclasses import dataclass
from typing import Dict

import pandas as pd

from finstmt.bs.data import BalanceSheetData
from finstmt.findata.statementsbase import FinStatementsBase


@dataclass
class BalanceSheets(FinStatementsBase):
    """
    Main class for holding balance sheet data. Usual way to construct is with the .from_df method.

    Examples:
        >>> bs_path = r'WMT Balance Sheet.xlsx'
        >>> bs_df = pd.read_excel(bs_path)
        >>> bs_data = BalanceSheets.from_df(bs_df)
    """
    statements: Dict[pd.Timestamp, BalanceSheetData]  # type: ignore

    statement_cls = BalanceSheetData  # type: ignore
    statement_name = 'Balance Sheet'
