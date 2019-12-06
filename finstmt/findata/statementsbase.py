from typing import Dict, Tuple
from dataclasses import field

import pandas as pd

from finstmt.config_manage.statement import StatementConfigManager
from finstmt.findata.database import FinDataBase
from finstmt.forecast.config import ForecastConfig
from finstmt.forecast.main import Forecast


class FinStatementsBase:
    statement_cls = FinDataBase  # to be overridden with individual class
    statements: Dict[pd.Timestamp, FinDataBase]

    def __post_init__(self):
        self.df = self.to_df()

        # Hook up prior statements to statements
        dates = list(self.statements.keys())
        dates.sort()
        prior_date = None
        for i, date in enumerate(dates):
            if i != 0:
                self.statements[date].prior_statement = self.statements[prior_date]
            prior_date = date

        # Create dictionary of individual time period configs to construct the entire statement config
        configs_dict = {}
        for date, statement in self.statements.items():
            configs_dict[date] = statement.items_config
        self.config = StatementConfigManager(configs_dict)

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
            date_item = pd.to_datetime(item)
            return self.statements[date_item]

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

    def _forecast(self, statements, **kwargs) -> Tuple[Dict[str, Forecast], Dict[str, pd.Series], Dict[str, pd.Series]]:
        forecast_config = ForecastConfig(**kwargs)
        forecast_dict = {}
        results = {}
        pct_results = {}
        for item in self.statement_cls.items_config:
            if item.extract_names is None or not item.forecast_config.make_forecast:
                # If can't extract item, must be calculated item, no need to forecast
                continue
            data = getattr(statements, item.key)
            pct_of_series = None
            if item.forecast_config.pct_of is not None:
                pct_of_series = getattr(statements, item.forecast_config.pct_of)
            forecast = Forecast(data, forecast_config, item.forecast_config, pct_of_series=pct_of_series)
            forecast.fit()
            forecast_dict[item.key] = forecast
            forecast.result.name = item.primary_name
            if item.forecast_config.pct_of is not None:
                pct_results[item.key] = forecast.result
            else:
                results[item.key] = forecast.result

        return forecast_dict, results, pct_results



