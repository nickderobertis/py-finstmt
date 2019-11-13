import datetime
from dataclasses import dataclass
from typing import List, Dict

import pandas as pd

from finstmt.inc.data import IncomeStatementData


@dataclass
class IncomeStatements:
    statements: Dict[pd.Timestamp, IncomeStatementData]

    @classmethod
    def from_df(cls, df: pd.DataFrame):
        statements_dict = {}
        for col in df.columns:
            statement = IncomeStatementData.from_series(df[col])
            statement_date = pd.to_datetime(col)
            statements_dict[statement_date] = statement
        return cls(statements_dict)

