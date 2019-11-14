from dataclasses import dataclass
from typing import Dict

import pandas as pd

from finstmt.bs.data import BalanceSheetData
from finstmt.findata.statementsbase import FinStatementsBase


@dataclass
class BalanceSheets(FinStatementsBase):
    statements: Dict[pd.Timestamp, BalanceSheetData]

    statement_cls = BalanceSheetData
