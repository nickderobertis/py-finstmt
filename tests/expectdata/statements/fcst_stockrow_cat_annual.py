import pandas as pd

FCST_STOCKROW_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_A_INDEX_str]
FCST_STOCKROW_CAT_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    rd_exp=pd.Series(
        [2130500387.0127494, 1973828594.92464],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    op_exp=pd.Series(
        [7836273227.615419, 7916844971.076348],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    ebit=pd.Series(
        [9376308151.987875, 10562458842.69706],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [509060669.62063605, 527160678.1193687],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    ebt=pd.Series(
        [8867247482.367239, 10035298164.57769],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [3291828332.091719, 3725449062.3877163],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [5575419150.27552, 6309849102.189974],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash=pd.Series(
        [7596595719.159299, 7787233824.468133],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [7596595719.159299, 7787233824.468133],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_current_assets=pd.Series(
        [57070403539.95273, 59890548696.76419],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gross_ppe=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    dep=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [1301450391.2211661, 1177048728.846231],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [23311444914.654552, 23313086931.598053],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_assets=pd.Series(
        [80381848454.60728, 83203635628.36224],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403369],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_debt=pd.Series(
        [12855056751.173033, 13340874057.502144],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_current_liab=pd.Series(
        [20359982971.008095, 21359409064.905514],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [27729931899.19445, 28687142277.64022],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [40584988650.367485, 42028016335.142365],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [29451131899.19445, 30408342277.64022],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [49811114870.202545, 51767751342.545746],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [80381848203.53589, 83203636191.03061],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
)
