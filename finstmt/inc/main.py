import datetime
from dataclasses import dataclass
from typing import List, Dict

import pandas as pd

from finstmt.inc.data import IncomeStatementData


@dataclass
class IncomeStatements:
    statements: Dict[pd.Timestamp, IncomeStatementData]

    def __post_init__(self):
        self.df = self.to_df()

    def _repr_html_(self):
        return self.df._repr_html_()

    @classmethod
    def from_df(cls, df: pd.DataFrame):
        statements_dict = {}
        for col in df.columns:
            statement = IncomeStatementData.from_series(df[col])
            statement_date = pd.to_datetime(col)
            statements_dict[statement_date] = statement
        return cls(statements_dict)

    def to_df(self) -> pd.DataFrame:
        all_series = []
        for date, statement in self.statements.items():
            series = statement.to_series()
            series.name = date
            all_series.append(series)
        return pd.concat(all_series, axis=1)
