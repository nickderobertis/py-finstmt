from typing import Dict

import pandas as pd
from pandas.testing import assert_series_equal

from finstmt import FinancialStatements, IncomeStatements, BalanceSheets


class LoadTest:
    a_test_data_dict: Dict[str, pd.Series]
    q_test_data_dict: Dict[str, pd.Series]

    def test_annual(self, stmts: FinancialStatements):
        raise NotImplementedError

    def test_quarterly(self, stmts: FinancialStatements):
        raise NotImplementedError

    def check_data_items(self, stmts: FinancialStatements, data_dict: Dict[str, pd.Series]):
        for item_key, item_values in data_dict.items():
            item = getattr(stmts, item_key)
            assert_series_equal(item, item_values)



class TestLoadStockrow(LoadTest):
    a_index_str = [
        '2009-12-31T00:00:00.000000000', '2010-12-31T00:00:00.000000000',
        '2011-12-31T00:00:00.000000000', '2012-12-31T00:00:00.000000000',
        '2013-12-31T00:00:00.000000000', '2014-12-31T00:00:00.000000000',
        '2015-12-31T00:00:00.000000000', '2016-12-31T00:00:00.000000000',
        '2017-12-31T00:00:00.000000000', '2018-12-31T00:00:00.000000000'
    ]
    a_index = [pd.to_datetime(index_str) for index_str in a_index_str]
    a_test_data_dict = dict(
        revenue=pd.Series(
            [3.2396e+10, 4.2588e+10, 6.0138e+10, 6.5875e+10, 5.5656e+10,
             5.5184e+10, 4.7011e+10, 3.8537e+10, 4.5462e+10, 5.4722e+10],
            index=a_index
        )
    )

    q_index_str = [
        '2009-12-31T00:00:00.000000000', '2010-03-31T00:00:00.000000000',
        '2010-06-30T00:00:00.000000000', '2010-09-30T00:00:00.000000000',
        '2010-12-31T00:00:00.000000000', '2011-03-31T00:00:00.000000000',
        '2011-06-30T00:00:00.000000000', '2011-09-30T00:00:00.000000000',
        '2011-12-31T00:00:00.000000000', '2012-03-31T00:00:00.000000000',
        '2012-06-30T00:00:00.000000000', '2012-09-30T00:00:00.000000000',
        '2012-12-31T00:00:00.000000000', '2013-03-31T00:00:00.000000000',
        '2013-06-30T00:00:00.000000000', '2013-09-30T00:00:00.000000000',
        '2013-12-31T00:00:00.000000000', '2014-03-31T00:00:00.000000000',
        '2014-06-30T00:00:00.000000000', '2014-09-30T00:00:00.000000000',
        '2014-12-31T00:00:00.000000000', '2015-03-31T00:00:00.000000000',
        '2015-06-30T00:00:00.000000000', '2015-09-30T00:00:00.000000000',
        '2015-12-31T00:00:00.000000000', '2016-03-31T00:00:00.000000000',
        '2016-06-30T00:00:00.000000000', '2016-09-30T00:00:00.000000000',
        '2016-12-31T00:00:00.000000000', '2017-03-31T00:00:00.000000000',
        '2017-06-30T00:00:00.000000000', '2017-09-30T00:00:00.000000000',
        '2017-12-31T00:00:00.000000000', '2018-03-31T00:00:00.000000000',
        '2018-06-30T00:00:00.000000000', '2018-09-30T00:00:00.000000000',
        '2018-12-31T00:00:00.000000000', '2019-03-31T00:00:00.000000000',
        '2019-06-30T00:00:00.000000000', '2019-09-30T00:00:00.000000000'
    ]
    q_index = [pd.to_datetime(index_str) for index_str in q_index_str]
    q_test_data_dict = dict(
        revenue=pd.Series(
            [7.8980e+09, 8.2380e+09, 1.0409e+10, 1.1134e+10, 1.2807e+10,
             1.2949e+10, 1.4230e+10, 1.5716e+10, 1.7243e+10, 1.5981e+10,
             1.7374e+10, 1.6445e+10, 1.6075e+10, 1.3210e+10, 1.4621e+10,
             1.3423e+10, 1.4402e+10, 1.3241e+10, 1.4150e+10, 1.3549e+10,
             1.4244e+10, 1.2702e+10, 1.2317e+10, 1.0962e+10, 1.1030e+10,
             9.4610e+09, 1.0342e+10, 9.1600e+09, 9.5740e+09, 9.8220e+09,
             1.1331e+10, 1.1413e+10, 1.2896e+10, 1.2859e+10, 1.4011e+10,
             1.3510e+10, 1.4342e+10, 1.3466e+10, 1.4432e+10, 1.2758e+10],
            index=q_index
        )
    )


    def test_annual(self, annual_stockrow_stmts):
        self.check_data_items(annual_stockrow_stmts, self.a_test_data_dict)

    def test_quarterly(self, quarterly_stockrow_stmts: FinancialStatements):
        self.check_data_items(quarterly_stockrow_stmts, self.q_test_data_dict)


class TestLoadCapitalIQ:

    def test_annual(self, annual_capiq_income_df, annual_capiq_bs_df):
        bs = BalanceSheets.from_df(annual_capiq_bs_df)
        inc = IncomeStatements.from_df(annual_capiq_income_df)
        stmts = FinancialStatements(inc, bs)

    def test_quarterly(self, quarterly_capiq_income_df, quarterly_capiq_bs_df):
        bs = BalanceSheets.from_df(quarterly_capiq_bs_df)
        inc = IncomeStatements.from_df(quarterly_capiq_income_df)
        stmts = FinancialStatements(inc, bs)