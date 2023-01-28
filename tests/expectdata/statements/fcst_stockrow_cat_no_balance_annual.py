import pandas as pd

FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_str = [
    "2019-12-31 00:00:00",
    "2020-12-31 00:00:00",
]
FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX = [
    pd.to_datetime(val) for val in FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_str
]
FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    rd_exp=pd.Series(
        [2130504180.795485, 1973832561.7877598],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    dep_exp=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    other_op_exp=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    op_exp=pd.Series(
        [7836277021.398155, 7916848937.939468],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    ebit=pd.Series(
        [9376304358.20514, 10562454875.833939],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    int_exp=pd.Series(
        [465174147.18453807, 471960192.16392887],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    gain_on_sale_invest=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    gain_on_sale_asset=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    impairment=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    ebt=pd.Series(
        [8911130211.020601, 10090494683.67001],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    tax_exp=pd.Series(
        [3308119115.6474824, 3745939915.467237],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    net_income=pd.Series(
        [5603011095.373119, 6344554768.202773],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    cash=pd.Series(
        [8828000000.000004, 9339018181.818186],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    st_invest=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    cash_and_st_invest=pd.Series(
        [8828000000.000004, 9339018181.818186],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    def_tax_st=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    other_current_assets=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    total_current_assets=pd.Series(
        [58301807820.79343, 61442333054.11424],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    gross_ppe=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    dep=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX
    ),
    lt_invest=pd.Series([0.0, 0.0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    def_tax_lt=pd.Series(
        [1301450391.2211661, 1177048728.846231],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    other_lt_assets=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    total_non_current_assets=pd.Series(
        [23311444914.654552, 23313086931.598053],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    total_assets=pd.Series(
        [81613252735.44798, 84755419985.7123],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    payables=pd.Series(
        [7504926219.835061, 8018535007.403371],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    st_debt=pd.Series(
        [11746812154.4178, 11943913393.304644],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    current_lt_debt=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    tax_liab_st=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    other_current_liab=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    total_current_liab=pd.Series(
        [19251738374.252865, 19962448400.708015],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    lt_debt=pd.Series(
        [25339312566.232864, 25683230453.16987],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    total_debt=pd.Series(
        [37086124720.650665, 37627143846.47451],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    deferred_rev=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    tax_liab_lt=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX
    ),
    other_lt_liab=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    total_non_current_liab=pd.Series(
        [27060512566.23287, 27404430453.16987],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    total_liab=pd.Series(
        [46312250940.48573, 47366878853.877884],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    common_stock=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    minority_interest=pd.Series([0, 0], index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
    total_liab_and_equity=pd.Series(
        [76882984273.81908, 78802763702.36275],
        index=FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX,
    ),
)
