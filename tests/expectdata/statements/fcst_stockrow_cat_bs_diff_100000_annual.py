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
        [509060009.66850644, 527159839.26458526],
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
        [8867248142.319368, 10035299003.432474],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    tax_exp=pd.Series(
        [3291828577.088729, 3725449373.7995663],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    net_income=pd.Series(
        [5575419565.23064, 6309849629.632908],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    cash=pd.Series(
        [7596614433.599687, 7787257532.033208],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [7596614433.599687, 7787257532.033208],
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
        [57070422254.39311, 59890572404.32927],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    gross_ppe=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    dep=pd.Series(
        [13698894523.433386, 13824938202.751822],
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
        [23311444914.654552, 23313086931.598053],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_assets=pd.Series(
        [80381867169.04767, 83203659335.92732],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403369],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    st_debt=pd.Series(
        [12855040085.72904, 13340852828.574263],
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
        [20359966305.564102, 21359387835.97763],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    lt_debt=pd.Series(
        [27729895949.790573, 28687096628.661606],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_debt=pd.Series(
        [40584936035.519615, 42027949457.23587],
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
        [29451095949.790573, 30408296628.661606],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
    total_liab=pd.Series(
        [49811062255.354675, 51767684464.63924],
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
        [80381795588.68802, 83203569313.1241],
        index=FCST_STOCKROW_CAT_BS_DIFF_100000_A_INDEX
    ),
)
