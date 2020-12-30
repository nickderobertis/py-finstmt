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
        [9376308151.987877, 10562458842.69706],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [531281196.21853375, 555071035.030807],
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
        [8845026955.769342, 10007387807.666252],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [3283579305.6430473, 3715087774.533446],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [5561447650.126295, 6292300033.132807],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash=pd.Series(
        [9368129050.086632, 10012396889.216621],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [9368129050.086632, 10012396889.216621],
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
        [58841936870.88006, 62115711761.51268],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gross_ppe=pd.Series(
        [13698894523.433386, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    dep=pd.Series(
        [0.0, 13824938202.751822],
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
        [82153381785.5346, 85428798693.11073],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403369],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_debt=pd.Series(
        [13416180694.748941, 14047202453.967098],
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
        [20921106914.584, 22065737461.37047],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [28940344971.929237, 30205974036.098587],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [42356525666.67818, 44253176490.06569],
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
        [30661544971.929237, 31927174036.098587],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [51582651886.51324, 53992911497.469055],
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
        [82153385219.84659, 85428796345.95392],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
)
