import pandas as pd

STOCKROW_FCST_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
STOCKROW_FCST_CAT_Q_INDEX = [pd.to_datetime(val) for val in STOCKROW_FCST_CAT_Q_INDEX_str]
STOCKROW_FCST_CAT_Q_INDEX_DATA_DICT = dict(
        revenue=pd.Series(
                [12911872667.210337, 13067601173.714796],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        cogs=pd.Series(
                [9037499726.12271, 9129684386.837868],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        gross_profit=pd.Series(
                [3874372941.0876274, 3937916786.8769283],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        rd_exp=pd.Series(
                [556710471.3403659, 476761184.9890613],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        sga=pd.Series(
                [1259904043.8414893, 1268871462.5804458],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        dep_exp=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_op_exp=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        op_exp=pd.Series(
                [1816614515.1818552, 1745632647.5695071],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        ebit=pd.Series(
                [2057758425.9057722, 2192284139.307421],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        int_exp=pd.Series(
                [117698628.55091406, 82301311.76969934],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        gain_on_sale_invest=pd.Series(
                [-0.0, -0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        gain_on_sale_asset=pd.Series(
                [-0.0, -0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        impairment=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        ebt=pd.Series(
                [1940059797.3548582, 2109982827.5377219],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        tax_exp=pd.Series(
                [655344190.8995498, 712743489.0460389],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        net_income=pd.Series(
                [1284715606.4553082, 1397239338.491683],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        cash=pd.Series(
                [8928169230.769226, 13022957785.859406],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        st_invest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        cash_and_st_invest=pd.Series(
                [8928169230.769226, 13022957785.859406],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        receivables=pd.Series(
                [32121906078.42198, 32509324432.722553],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        inventory=pd.Series(
                [11817497605.12702, 11966311963.142391],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        def_tax_st=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_current_assets=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_current_assets=pd.Series(
                [52867572914.31823, 57498594181.72435],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        gross_ppe=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        dep=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        net_ppe=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        goodwill=pd.Series(
                [8462500000.0, 8462500000.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        lt_invest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        def_tax_lt=pd.Series(
                [1336374408.7046144, 1301673877.7263904],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_lt_assets=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_non_current_assets=pd.Series(
                [9798874408.704615, 9764173877.72639],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_assets=pd.Series(
                [62666447323.02284, 67262768059.450745],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        payables=pd.Series(
                [6762939214.231988, 6872127631.8362055],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        st_debt=pd.Series(
                [12389396735.328045, 8674036257.122883],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        current_lt_debt=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        tax_liab_st=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_current_liab=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_current_liab=pd.Series(
                [19152335949.56003, 15546163888.959091],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        lt_debt=pd.Series(
                [25689310937.859745, 17952676650.093365],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_debt=pd.Series(
                [38078707673.18779, 26626712907.216248],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        deferred_rev=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        tax_liab_lt=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        deposit_liab=pd.Series(
                [1839275000.0, 1839275000.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_lt_liab=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_non_current_liab=pd.Series(
                [27528585937.859745, 19791951650.093365],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_liab=pd.Series(
                [46680921887.41978, 35338115539.05246],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        common_stock=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        other_income=pd.Series(
                [-1750003375.5336783, -1717617394.4920182],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        retained_earnings=pd.Series(
                [33410292307.69231, 33642269981.238277],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        minority_interest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_equity=pd.Series(
                [31660288932.15863, 31924652586.746258],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
        total_liab_and_equity=pd.Series(
                [78341210819.5784, 67262768125.79872],
                index=STOCKROW_FCST_CAT_Q_INDEX
        ),
)