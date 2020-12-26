import pandas as pd

FCST_STOCKROW_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_STOCKROW_CAT_Q_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_Q_INDEX_str]
FCST_STOCKROW_CAT_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [12911872667.210337, 13067601173.714796],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cogs=pd.Series(
        [9037499726.122707, 9129684386.837864],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gross_profit=pd.Series(
        [3874372941.0876293, 3937916786.876932],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    rd_exp=pd.Series(
        [556710471.3392289, 476761184.98755884],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    sga=pd.Series(
        [1259904043.8414893, 1268871462.5804458],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    op_exp=pd.Series(
        [1816614515.1807182, 1745632647.5680046],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    ebit=pd.Series(
        [2057758425.9069111, 2192284139.3089275],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    int_exp=pd.Series(
        [111276126.67002212, 112091192.7684246],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    ebt=pd.Series(
        [1946482299.2368891, 2080192946.540503],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_exp=pd.Series(
        [594701668.0653028, 635553796.5540773],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    net_income=pd.Series(
        [1351780631.1715863, 1444639149.9864256],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash=pd.Series(
        [9638464750.125027, 9730171857.126688],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [9638464750.125027, 9730171857.126688],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    receivables=pd.Series(
        [32121906078.42198, 32509324432.722553],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    inventory=pd.Series(
        [11817497605.127018, 11966311963.142387],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_current_assets=pd.Series(
        [53577868433.67403, 54205808252.99163],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gross_ppe=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    dep=pd.Series(
        [12853612568.208256, 12865235637.252861],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    net_ppe=pd.Series(
        [12853612568.208256, 12865235637.252861],
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
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_non_current_assets=pd.Series(
        [22652486976.912872, 22629409514.97925],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_assets=pd.Series(
        [76230355410.5869, 76835217767.97089],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    payables=pd.Series(
        [6762939214.231989, 6872127631.8362055],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_debt=pd.Series(
        [11713340227.147573, 11813700769.413826],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_current_liab=pd.Series(
        [18476279441.379562, 18685828401.250034],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    lt_debt=pd.Series(
        [24287513399.107193, 24450848909.016846],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_debt=pd.Series(
        [36000853626.25477, 36264549678.43067],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    deposit_liab=pd.Series(
        [1839275000.0, 1839275000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_non_current_liab=pd.Series(
        [26126788399.107193, 26290123909.016846],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_liab=pd.Series(
        [44603067840.486755, 44975952310.26688],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    other_income=pd.Series(
        [-1783000000.0, -1783000000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    retained_earnings=pd.Series(
        [33410292307.692314, 33642269981.23828],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_equity=pd.Series(
        [31627292307.692314, 31859269981.23828],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [76230360148.17908, 76835222291.50516],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
)
