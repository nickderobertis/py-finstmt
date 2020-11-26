import pandas as pd

FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX_str]
FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    rd_exp=pd.Series(
        [2130500387.0127494, 1973828594.92464],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    op_exp=pd.Series(
        [7836273227.615419, 7916844971.076348],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    ebit=pd.Series(
        [9376308151.987875, 10562458842.69706],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    int_exp=pd.Series(
        [465174147.1845382, 527160676.9173279],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    ebt=pd.Series(
        [8911134004.803337, 10035298165.779732],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    tax_exp=pd.Series(
        [3308120524.030582, 3725449062.833956],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    net_income=pd.Series(
        [5603013480.772755, 6309849102.945776],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    cash=pd.Series(
        [8828000000.000002, 7787234307.869675],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [8828000000.000002, 7787234307.869675],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_current_assets=pd.Series(
        [58301807820.79343, 59890549180.16573],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    gross_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    dep=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [1301450391.2211661, 1177048728.846231],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [23311444914.654552, 23313086931.59806],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_assets=pd.Series(
        [81613252735.44798, 83203636111.7638],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403369],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    st_debt=pd.Series(
        [11746812154.417807, 13340874027.082022],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_current_liab=pd.Series(
        [19251738374.252865, 21359409034.485382],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    lt_debt=pd.Series(
        [25339312566.23287, 28687142212.227234],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_debt=pd.Series(
        [37086124720.65067, 42028016239.30926],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [27060512566.23287, 30408342212.227234],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_liab=pd.Series(
        [46312250940.48573, 51767751246.712616],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [76882984273.81908, 83203636095.19748],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
)
