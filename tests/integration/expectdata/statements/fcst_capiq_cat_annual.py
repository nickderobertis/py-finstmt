import pandas as pd

FCST_CAPIQ_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_CAPIQ_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_A_INDEX_str]
FCST_CAPIQ_CAT_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [54630.06518336638, 54538.284820343906], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    cogs=pd.Series(
        [36258.93669756556, 35382.62984773563], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gross_profit=pd.Series(
        [18371.128485800822, 19155.654972608274], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    rd_exp=pd.Series(
        [1660.4874275857828, 1349.0032098336733], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    sga=pd.Series([4613.797118402208, 4429.280867618918], index=FCST_CAPIQ_CAT_A_INDEX),
    dep_exp=pd.Series([0, 0], index=FCST_CAPIQ_CAT_A_INDEX),
    other_op_exp=pd.Series([51.4, 51.4], index=FCST_CAPIQ_CAT_A_INDEX),
    op_exp=pd.Series(
        [6325.684545987991, 5829.684077452594], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    ebit=pd.Series(
        [12045.44393981283, 13325.97089515568], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [94.76554690770718, 90.68363007665315], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gain_on_sale_invest=pd.Series([83.4, 83.4], index=FCST_CAPIQ_CAT_A_INDEX),
    gain_on_sale_asset=pd.Series([0, 0], index=FCST_CAPIQ_CAT_A_INDEX),
    impairment=pd.Series([119.0, 119.0], index=FCST_CAPIQ_CAT_A_INDEX),
    ebt=pd.Series(
        [11950.678392905123, 13235.287265079029], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [7075.175838800857, 7835.7045180856985], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [4875.502554104267, 5399.58274699333], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    cash=pd.Series(
        [10459.995672597433, 10742.59804190024], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    st_invest=pd.Series([0, 0], index=FCST_CAPIQ_CAT_A_INDEX),
    cash_and_st_invest=pd.Series(
        [10459.995672597433, 10742.59804190024], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    receivables=pd.Series(
        [8266.894222673915, 8253.005559896765], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    inventory=pd.Series(
        [11708.880980931483, 11651.321876515996], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    def_tax_st=pd.Series([328.8, 328.8], index=FCST_CAPIQ_CAT_A_INDEX),
    other_current_assets=pd.Series([26.2, 26.2], index=FCST_CAPIQ_CAT_A_INDEX),
    total_current_assets=pd.Series(
        [30790.77087620283, 31001.925478313], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    gross_ppe=pd.Series([31361.6, 31361.6], index=FCST_CAPIQ_CAT_A_INDEX),
    dep=pd.Series([16218.0, 16218.0], index=FCST_CAPIQ_CAT_A_INDEX),
    net_ppe=pd.Series(
        [15143.599999999999, 15143.599999999999], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    goodwill=pd.Series([6335.6, 6335.6], index=FCST_CAPIQ_CAT_A_INDEX),
    lt_invest=pd.Series([0.0, 0.0], index=FCST_CAPIQ_CAT_A_INDEX),
    def_tax_lt=pd.Series(
        [1383.055805600257, 1403.4067215000555], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    other_lt_assets=pd.Series([1168.6, 1168.6], index=FCST_CAPIQ_CAT_A_INDEX),
    total_non_current_assets=pd.Series(
        [24030.855805600255, 24051.206721500053], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_assets=pd.Series(
        [54821.626681803085, 55053.13219981306], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    payables=pd.Series(
        [7673.534479950697, 7973.8378874981], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    st_debt=pd.Series([0.0, 0.0], index=FCST_CAPIQ_CAT_A_INDEX),
    current_lt_debt=pd.Series(
        [58.95668581440481, 56.41719444879978], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    tax_liab_st=pd.Series([82.8, 82.8], index=FCST_CAPIQ_CAT_A_INDEX),
    other_current_liab=pd.Series([3499.0, 3499.0], index=FCST_CAPIQ_CAT_A_INDEX),
    total_current_liab=pd.Series(
        [11314.291165765098, 11612.055081946897], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [7223.835516037975, 6912.6771178661575], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [7223.835516037975, 6912.6771178661575], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    deferred_rev=pd.Series([0, 0], index=FCST_CAPIQ_CAT_A_INDEX),
    tax_liab_lt=pd.Series([82.8, 82.8], index=FCST_CAPIQ_CAT_A_INDEX),
    deposit_liab=pd.Series([0, 0], index=FCST_CAPIQ_CAT_A_INDEX),
    other_lt_liab=pd.Series([3236.0, 3236.0], index=FCST_CAPIQ_CAT_A_INDEX),
    total_non_current_liab=pd.Series(
        [10542.635516037975, 10231.477117866158], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [21856.926681803074, 21843.532199813053], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    common_stock=pd.Series([5983.3, 6181.0], index=FCST_CAPIQ_CAT_A_INDEX),
    other_income=pd.Series(
        [424.90000000000146, 1458.6000000000022], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    retained_earnings=pd.Series(
        [26488.100000000002, 25501.600000000006], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    minority_interest=pd.Series([68.4, 68.4], index=FCST_CAPIQ_CAT_A_INDEX),
    total_equity=pd.Series(
        [32964.700000000004, 33209.600000000006], index=FCST_CAPIQ_CAT_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [54821.62668180308, 55053.13219981306], index=FCST_CAPIQ_CAT_A_INDEX
    ),
)
