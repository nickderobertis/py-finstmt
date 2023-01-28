import pandas as pd

FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_str = [
    "2019-12-31 00:00:00",
    "2020-12-31 00:00:00",
]
FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX = [
    pd.to_datetime(val) for val in FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_str
]
FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    rd_exp=pd.Series(
        [2130504180.795485, 1973832561.7877598],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    dep_exp=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    other_op_exp=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    op_exp=pd.Series(
        [7836277021.398155, 7916848937.939468],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    ebit=pd.Series(
        [9376304358.20514, 10562454875.833939],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    int_exp=pd.Series(
        [598429523.6351757, 1073345677.2586178],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    impairment=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    ebt=pd.Series(
        [8777874834.569963, 9489109198.575321],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    tax_exp=pd.Series(
        [3258650120.3954573, 3522684865.658373],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    net_income=pd.Series(
        [5519224714.174506, 5966424332.916948],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    cash=pd.Series(
        [8828000000.000004, 9339018181.818184],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    st_invest=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    cash_and_st_invest=pd.Series(
        [8828000000.000004, 9339018181.818184],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    def_tax_st=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    other_current_assets=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_current_assets=pd.Series(
        [58301807820.79343, 61442333054.11424],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    gross_ppe=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    dep=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    lt_invest=pd.Series([0.0, 0.0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    def_tax_lt=pd.Series(
        [7195000000.0, 43170000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    other_lt_assets=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [29204994523.433388, 65306038202.75182],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    total_assets=pd.Series(
        [87506802344.2268, 126748371256.86606],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    payables=pd.Series(
        [7504926219.835061, 8018535007.403371],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    st_debt=pd.Series(
        [22370630224.82554, 59889520947.80798],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    current_lt_debt=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    tax_liab_st=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    other_current_liab=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_current_liab=pd.Series(
        [29875556444.6606, 67908055955.21136],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    lt_debt=pd.Series(
        [25339312566.232864, 25683230453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    total_debt=pd.Series(
        [47709942791.0584, 85572751400.97784],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    deferred_rev=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    tax_liab_lt=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_lt_liab=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    total_non_current_liab=pd.Series(
        [27060512566.232864, 27404430453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    total_liab=pd.Series(
        [56936069010.89346, 95312486408.38123],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    common_stock=pd.Series([0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    minority_interest=pd.Series(
        [0, 0], index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
    total_liab_and_equity=pd.Series(
        [87506802344.2268, 126748371256.86609],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
    ),
)
