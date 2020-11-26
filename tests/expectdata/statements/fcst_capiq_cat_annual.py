import pandas as pd

FCST_CAPIQ_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_CAPIQ_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_A_INDEX_str]
FCST_CAPIQ_CAT_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [54630.06518336638, 54538.284820343906],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    cogs=pd.Series(
        [36258.93669756556, 35382.62984773563],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gross_profit=pd.Series(
        [18371.128485800822, 19155.654972608274],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    rd_exp=pd.Series(
        [1660.4438910340386, 1348.959364124922],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    sga=pd.Series(
        [4613.797118402208, 4429.280867618918],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_op_exp=pd.Series(
        [51.4, 51.4],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    op_exp=pd.Series(
        [6325.641009436247, 5829.640231743841],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    ebit=pd.Series(
        [12045.487476364575, 13326.014740864433],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [94.76554690770718, 90.68363007665357],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [83.4, 83.4],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    impairment=pd.Series(
        [119.0, 119.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    ebt=pd.Series(
        [11950.721929456868, 13235.33111078778],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [7075.2016138028175, 7835.730476118288],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [4875.52031565405, 5399.600634669492],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    cash=pd.Series(
        [7255.5, 7589.799999999999],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [7255.5, 7589.799999999999],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    receivables=pd.Series(
        [8266.894222673915, 8253.005559896765],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    inventory=pd.Series(
        [11708.880980931483, 11651.321876515996],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    def_tax_st=pd.Series(
        [328.8, 328.8],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_current_assets=pd.Series(
        [26.2, 26.2],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_current_assets=pd.Series(
        [27586.275203605397, 27849.12743641276],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gross_ppe=pd.Series(
        [31361.6, 31361.6],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    dep=pd.Series(
        [16218.0, 16218.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    net_ppe=pd.Series(
        [15143.599999999999, 15143.599999999999],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    goodwill=pd.Series(
        [6335.6, 6335.6],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [1383.055805600257, 1403.4067215000555],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [1168.6, 1168.6],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [24030.855805600255, 24051.206721500053],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_assets=pd.Series(
        [51617.13100920565, 51900.33415791282],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    payables=pd.Series(
        [7673.534479950697, 7973.8378874981],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    st_debt=pd.Series(
        [0.0, 0.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [58.95668581440441, 56.41719444879978],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [82.8, 82.8],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_current_liab=pd.Series(
        [3499.0, 3499.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_current_liab=pd.Series(
        [11314.2911657651, 11612.055081946897],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [7223.835516037972, 6912.6771178661575],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [7223.835516037972, 6912.6771178661575],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [82.8, 82.8],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [3236.0, 3236.0],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [10542.635516037972, 10231.477117866158],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [21856.926681803074, 21843.532199813053],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    common_stock=pd.Series(
        [5983.3, 6181.000000000001],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_income=pd.Series(
        [424.90000000000146, 1458.6000000000022],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    retained_earnings=pd.Series(
        [26488.1, 25501.600000000002],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    minority_interest=pd.Series(
        [68.4, 68.4],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_equity=pd.Series(
        [32964.7, 33209.600000000006],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [54821.62668180307, 55053.13219981306],
        index=FCST_CAPIQ_CAT_A_INDEX
    ),
)
