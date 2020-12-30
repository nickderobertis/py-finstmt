import pandas as pd

FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_str]
FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [57667220437.771454, 60770957074.275894],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    rd_exp=pd.Series(
        [2130500387.0127494, 1973828594.92464],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    op_exp=pd.Series(
        [7836273227.615419, 7916844971.076348],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    ebit=pd.Series(
        [9376308151.987875, 10562458842.69706],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    int_exp=pd.Series(
        [598429523.6351757, 1073345677.2586173],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    ebt=pd.Series(
        [8777878628.3527, 9489113165.438442],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    tax_exp=pd.Series(
        [3258651528.778556, 3522686338.2948866],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    net_income=pd.Series(
        [5519227099.574144, 5966426827.143556],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    cash=pd.Series(
        [8828000000.000002, 9339018181.818176],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [8828000000.000002, 9339018181.818176],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_current_assets=pd.Series(
        [58301807820.79343, 61442333054.114235],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    gross_ppe=pd.Series(
        [13698894523.433386, 0.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    dep=pd.Series(
        [0.0, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [7195000000.0, 43170000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [29204994523.433388, 65306038202.75182],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_assets=pd.Series(
        [87506802344.2268, 126748371256.86606],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    payables=pd.Series(
        [7504926219.83506, 8018535007.403369],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    st_debt=pd.Series(
        [22370630224.82554, 59889520947.807945],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_current_liab=pd.Series(
        [29875556444.6606, 67908055955.21131],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    lt_debt=pd.Series(
        [25339312566.232864, 25683230453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_debt=pd.Series(
        [47709942791.0584, 85572751400.97781],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [27060512566.232864, 27404430453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_liab=pd.Series(
        [56936069010.89346, 95312486408.38118],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [87506802344.2268, 126748371256.86604],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX
    ),
)
