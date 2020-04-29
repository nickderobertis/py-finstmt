import pandas as pd

FCST_STOCKROW_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_STOCKROW_CAT_Q_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_Q_INDEX_str]
FCST_STOCKROW_CAT_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [12911872667.210337, 13067601173.714796],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cogs=pd.Series(
        [9037499726.12271, 9129684386.837868],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gross_profit=pd.Series(
        [3874372941.0876274, 3937916786.8769283],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    rd_exp=pd.Series(
        [556710471.3403659, 476761184.9890613],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    sga=pd.Series(
        [1259904043.8414893, 1268871462.5804458],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    dep_exp=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_op_exp=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    op_exp=pd.Series(
        [1816614515.1818552, 1745632647.5695071],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    ebit=pd.Series(
        [2057758425.9057722, 2192284139.307421],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    int_exp=pd.Series(
        [117698628.55091405, 82451941.61840512],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [-0.0, -0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [-0.0, -0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    impairment=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    ebt=pd.Series(
        [1940059797.3548582, 2109832197.689016],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_exp=pd.Series(
        [592739424.3891627, 644609369.3199522],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    net_income=pd.Series(
        [1347320372.9656954, 1465222828.369064],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash=pd.Series(
        [8928169230.769234, 13006308152.835913],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [8928169230.769234, 13006308152.835913],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    receivables=pd.Series(
        [32121906078.42198, 32509324432.722553],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    inventory=pd.Series(
        [11817497605.12702, 11966311963.142391],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    def_tax_st=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_current_assets=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_current_assets=pd.Series(
        [52867572914.31824, 57481944548.70086],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gross_ppe=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    dep=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    net_ppe=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    goodwill=pd.Series(
        [8462500000.0, 8462500000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    def_tax_lt=pd.Series(
        [1336374408.7046144, 1301673877.7263904],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_lt_assets=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_non_current_assets=pd.Series(
        [9798874408.704615, 9764173877.72639],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_assets=pd.Series(
        [62666447323.02285, 67246118426.427246],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    payables=pd.Series(
        [6762939214.231988, 6872127631.8362055],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_debt=pd.Series(
        [12389396735.328037, 8689911687.793226],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    current_lt_debt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_liab_st=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_current_liab=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_current_liab=pd.Series(
        [19152335949.560028, 15562039319.629433],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    lt_debt=pd.Series(
        [25689310937.859745, 17985534072.527077],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_debt=pd.Series(
        [38078707673.18778, 26675445760.320305],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    deposit_liab=pd.Series(
        [1839275000.0, 1839275000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_lt_liab=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_non_current_liab=pd.Series(
        [27528585937.859745, 19824809072.527077],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_liab=pd.Series(
        [46680921887.41977, 35386848392.15651],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    common_stock=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_income=pd.Series(
        [-1783000000.0, -1783000000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    retained_earnings=pd.Series(
        [33410292307.69231, 33642269981.238277],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    minority_interest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_equity=pd.Series(
        [31627292307.69231, 31859269981.238277],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [78308214195.11208, 67246118373.39479],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
)
