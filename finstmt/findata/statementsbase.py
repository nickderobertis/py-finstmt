from typing import Dict

import pandas as pd

from finstmt.findata.database import FinDataBase


class FinStatementsBase:
    statement_cls = FinDataBase  # to be overridden with individual class
    statements: Dict[pd.Timestamp, FinDataBase]

    def __post_init__(self):
        self.df = self.to_df()

    def _repr_html_(self):
        return self._formatted_df._repr_html_()

    def __getattr__(self, item):
        data_dict = {}
        for date, statement in self.statements.items():
            try:
                statement_value = getattr(statement, item)
            except AttributeError:
                # Should hit here on the first loop if this is an invalid item. Raise attribute error like normal.
                raise AttributeError(item)
            if pd.isnull(statement_value):
                statement_value = 0
            data_dict[date] = statement_value
            # TODO: set name of series
        return pd.Series(data_dict)

    def __getitem__(self, item):
        if not isinstance(item, (list, tuple)):
            series = self.df[item]
            date_item = pd.to_datetime(item)
            series.name = date_item
            return self.statement_cls.from_series(series)

        # Got multiple dates
        all_series = []
        for date_str in item:
            series = self.df[date_str]
            date = pd.to_datetime(date_str)
            series.name = date
            all_series.append(series)
        df = pd.concat(all_series, axis=1)

        return self.from_df(df)

    def __dir__(self):
        normal_attrs = [
            'statements',
            'to_df',
        ]
        item_attrs = dir(list(self.statements.values())[0])
        return normal_attrs + item_attrs

    @classmethod
    def from_df(cls, df: pd.DataFrame):
        """
        DataFrame must have columns as dates and index as names of financial statement items
        """
        statements_dict = {}
        for col in df.columns:
            statement = cls.statement_cls.from_series(df[col])
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

    @property
    def _formatted_df(self) -> pd.DataFrame:
        out_df = self.df.copy()
        out_df.columns = [col.strftime('%m/%d/%Y') for col in out_df.columns]
        return out_df.applymap(lambda x: f'${x:,.0f}' if not x == 0 else ' - ')
