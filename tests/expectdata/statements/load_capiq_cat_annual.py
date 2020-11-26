import pandas as pd

LOAD_CAPIQ_CAT_A_INDEX_str = ["2014-12-31 00:00:00", "2015-12-31 00:00:00", "2016-12-31 00:00:00", "2017-12-31 00:00:00", "2018-12-31 00:00:00"]
LOAD_CAPIQ_CAT_A_INDEX = [pd.to_datetime(val) for val in LOAD_CAPIQ_CAT_A_INDEX_str]
LOAD_CAPIQ_CAT_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [55184.0, 47011.0, 38537.0, 45462.0, 54722.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    cogs=pd.Series(
        [40718.0, 33546.0, 28044.0, 31260.0, 36997.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    gross_profit=pd.Series(
        [14466.0, 13465.0, 10493.0, 14202.0, 17725.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    rd_exp=pd.Series(
        [2380.0, 2119.0, 1853.0, 1842.0, 1850.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    sga=pd.Series(
        [5894.0, 4363.0, 4476.0, 4425.0, 4806.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    dep_exp=pd.Series(
        [0.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_op_exp=pd.Series(
        [44.0, 27.0, 78.0, 19.0, 89.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    op_exp=pd.Series(
        [8318.0, 6509.0, 6407.0, 6286.0, 6745.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    ebit=pd.Series(
        [3766.0, 4659.0, 1884.0, 5576.0, 8336.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    int_exp=pd.Series(
        [484.0, 507.0, 503.0, 531.0, 404.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [36.0, 176.0, 47.0, 187.0, -29.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    impairment=pd.Series(
        [0.0, 0.0, 595.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    ebt=pd.Series(
        [3160.0, 3439.0, 133.0, 4098.0, 7846.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    tax_exp=pd.Series(
        [692.0, 916.0, 192.0, 3339.0, 1698.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    net_income=pd.Series(
        [2452.0, 2512.0, -67.0, 754.0, 6147.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    cash=pd.Series(
        [6317.0, 5340.0, 5257.0, 7381.0, 6968.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    st_invest=pd.Series(
        [0.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [6317.0, 5340.0, 5257.0, 7381.0, 6968.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    receivables=pd.Series(
        [7699.0, 6677.0, 5919.0, 7376.0, 8714.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    inventory=pd.Series(
        [12205.0, 9700.0, 8614.0, 10018.0, 11529.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    def_tax_st=pd.Series(
        [1644.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_current_assets=pd.Series(
        [27.0, 14.0, 23.0, 48.0, 19.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_current_assets=pd.Series(
        [38867.0, 33508.0, 31967.0, 36244.0, 38603.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    gross_ppe=pd.Series(
        [31572.0, 31977.0, 31940.0, 31538.0, 29781.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    dep=pd.Series(
        [14995.0, 15887.0, 16618.0, 17383.0, 16207.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    net_ppe=pd.Series(
        [16577.0, 16090.0, 15322.0, 14155.0, 13574.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    goodwill=pd.Series(
        [6677.0, 6598.0, 6003.0, 6183.0, 6217.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    lt_invest=pd.Series(
        [257.0, 246.0, 249.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [1267.0, 2367.0, 2683.0, 1569.0, 1363.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [528.0, 1874.0, 1529.0, 950.0, 962.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [25306.0, 27175.0, 25786.0, 22857.0, 22116.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_assets=pd.Series(
        [84681.0, 78342.0, 74704.0, 76962.0, 78509.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    payables=pd.Series(
        [6515.0, 5023.0, 4614.0, 6487.0, 7051.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    st_debt=pd.Series(
        [9.0, 9.0, 209.0, 1.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [510.0, 517.0, 507.0, 6.0, 10.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [414.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_current_liab=pd.Series(
        [4004.0, 2955.0, 3377.0, 3424.0, 3735.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_current_liab=pd.Series(
        [27877.0, 26242.0, 26132.0, 26931.0, 28218.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    lt_debt=pd.Series(
        [9408.0, 8883.0, 8368.0, 7492.0, 7549.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_debt=pd.Series(
        [39293.0, 38017.0, 36784.0, 34880.0, 36593.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [414.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    deposit_liab=pd.Series(
        [0.0, 0.0, 0.0, 0.0, 0.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [2817.0, 3203.0, 3184.0, 3657.0, 3319.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [12639.0, 12086.0, 11552.0, 11149.0, 10868.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_liab=pd.Series(
        [67855.0, 63457.0, 61491.0, 63196.0, 64429.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    common_stock=pd.Series(
        [5016.0, 5238.0, 5277.0, 5593.0, 5827.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    other_income=pd.Series(
        [-6431.0, -2035.0, -2039.0, -1192.0, -1684.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    retained_earnings=pd.Series(
        [33887.0, 29246.0, 27377.0, 26301.0, 30427.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    minority_interest=pd.Series(
        [80.0, 76.0, 76.0, 69.0, 41.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_equity=pd.Series(
        [16826.0, 14885.0, 13213.0, 13766.0, 14080.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [84681.0, 78342.0, 74704.0, 76962.0, 78509.0],
        index=LOAD_CAPIQ_CAT_A_INDEX
    ),
)
