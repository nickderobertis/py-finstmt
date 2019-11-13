from dataclasses import dataclass
from typing import Dict

import pandas as pd

from finstmt.findata.statementsbase import FinStatementsBase
from finstmt.inc.data import IncomeStatementData


@dataclass
class IncomeStatements(FinStatementsBase):
    statements: Dict[pd.Timestamp, IncomeStatementData]

    statement_cls = IncomeStatementData
