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
        [117698628.55091408, 112091183.10479712],
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
        [1940059797.355997, 2080192956.2041304],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    tax_exp=pd.Series(
        [592739424.3895106, 635553799.5065703],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    net_income=pd.Series(
        [1347320372.9664865, 1444639156.69756],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash=pd.Series(
        [8928169230.76923, 9730173241.466858],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [8928169230.76923, 9730173241.466858],
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
        [52867572914.31822, 54205809637.3318],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    gross_ppe=pd.Series(
        [12853612568.208256, 12865235637.252861],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    dep=pd.Series(
        [0, 0],
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
        [22652486976.912872, 22629409514.979248],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_assets=pd.Series(
        [75520059891.2311, 76835219152.31105],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    payables=pd.Series(
        [6762939214.231989, 6872127631.8362055],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    st_debt=pd.Series(
        [12389396735.328045, 11813699750.928745],
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
        [19152335949.56004, 18685827382.76494],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    lt_debt=pd.Series(
        [25689310937.859753, 24450846801.055477],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_debt=pd.Series(
        [38078707673.1878, 36264546551.98422],
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
        [27528585937.859753, 26290121801.055477],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
    total_liab=pd.Series(
        [46680921887.41979, 44975949183.82042],
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
        [78308214195.1121, 76835219165.0587],
        index=FCST_STOCKROW_CAT_Q_INDEX
    ),
)
