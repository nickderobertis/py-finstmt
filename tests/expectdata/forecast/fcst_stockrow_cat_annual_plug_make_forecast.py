import pandas as pd

FCST_STOCKROW_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_A_INDEX_str]
FCST_STOCKROW_CAT_A_PLUG_MAKE_FORECAST_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cogs=pd.Series(
        [40454639058.16817, 42291653260.502495],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gross_profit=pd.Series(
        [17212581379.603287, 18479303813.7734],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    rd_exp=pd.Series(
        [2130500387.0127878, 1973828594.9246898],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    dep_exp=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_op_exp=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    op_exp=pd.Series(
        [7836273227.615458, 7916844971.076399],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    ebit=pd.Series(
        [9376308151.98783, 10562458842.697],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [465166202.18933624, 782798368.5639772],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [-0.0, -0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [-0.0, -0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    impairment=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    ebt=pd.Series(
        [8911141949.798492, 9779660474.133024],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [3308123473.4870176, 3630547527.967974],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [5603018476.311476, 6149112946.1650505],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash=pd.Series(
        [8828000000.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [8828000000.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    inventory=pd.Series(
        [12560519689.09872, 13203297991.089025],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    def_tax_st=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_current_assets=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_current_assets=pd.Series(
        [58301807820.79343, 52103314872.29606],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    gross_ppe=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    dep=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    net_ppe=pd.Series(
        [0.0, 0.0],
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
        [7195000000.0, 43170000000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [15506100000.0, 51481100000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_assets=pd.Series(
        [73807907820.79343, 103584414872.29605],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403367],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    st_debt=pd.Series(
        [11746178737.6969, 36725564410.850655],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_current_liab=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_current_liab=pd.Series(
        [19251104957.531967, 44744099418.25402],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [25339312566.232864, 25683230453.16987],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [37085491303.92976, 62408794864.02052],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [27060512566.232864, 27404430453.16987],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [46311617523.76483, 72148529871.42389],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    common_stock=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    retained_earnings=pd.Series(
        [32254733333.333347, 33119884848.484863],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    minority_interest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_equity=pd.Series(
        [30570733333.333347, 31435884848.484863],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [76882350857.09818, 103584414719.90875],
        index=FCST_STOCKROW_CAT_A_INDEX
    ),
)
