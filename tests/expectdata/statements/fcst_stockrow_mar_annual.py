import pandas as pd

FCST_STOCKROW_MAR_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_MAR_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_MAR_A_INDEX_str]
FCST_STOCKROW_MAR_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [20256466666.66667, 21313769696.969704],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    cogs=pd.Series(
        [16173270221.707315, 16774265514.320614],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    gross_profit=pd.Series(
        [4083196444.9593563, 4539504182.64909],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    rd_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    sga=pd.Series(
        [835333333.3333336, 853230303.0303032],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    op_exp=pd.Series(
        [835333333.3333336, 853230303.0303032],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    ebit=pd.Series(
        [3247863111.626023, 3686273879.618787],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    int_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    ebt=pd.Series(
        [3247863111.626023, 3686273879.618787],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    tax_exp=pd.Series(
        [995951943.821048, 1130389893.1950514],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    net_income=pd.Series(
        [2251911167.804975, 2555883986.4237356],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    cash=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    st_invest=pd.Series(
        [6280581868.665095, 9373795939.928816],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [6280581868.665095, 9373795939.928816],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    receivables=pd.Series(
        [2142889058.5516183, 2321276679.3028393],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    inventory=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_current_assets=pd.Series(
        [184800000.0, 184800000.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_current_assets=pd.Series(
        [8608270927.216713, 11879872619.231655],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    gross_ppe=pd.Series(
        [2028093740.9345036, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    dep=pd.Series(
        [0.0, 2102844694.2830825],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    net_ppe=pd.Series(
        [2028093740.9345036, 2102844694.2830825],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    goodwill=pd.Series(
        [17419000000.0, 17419000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    lt_invest=pd.Series(
        [732000000.0, 732000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    def_tax_lt=pd.Series(
        [143032821.016846, 119639695.25167897],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_lt_assets=pd.Series(
        [587000000.0, 587000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_non_current_assets=pd.Series(
        [20909126561.951347, 20960484389.53476],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_assets=pd.Series(
        [29517397489.16806, 32840357008.766415],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    payables=pd.Series(
        [502163717.91233855, 462537036.8423517],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    st_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    current_lt_debt=pd.Series(
        [776110714.178354, 887214695.3089366],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_current_liab=pd.Series(
        [2738275255.3015585, 2964868079.793126],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_current_liab=pd.Series(
        [4016549687.392251, 4314619811.944415],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    lt_debt=pd.Series(
        [9732820044.698414, 11126120040.225893],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_debt=pd.Series(
        [9732820044.698414, 11126120040.225893],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_lt_liab=pd.Series(
        [5773793951.4529295, 6285199206.98236],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_non_current_liab=pd.Series(
        [15506613996.151344, 17411319247.208252],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_liab=pd.Series(
        [19523163683.543594, 21725939059.152668],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    common_stock=pd.Series(
        [5000000.0, 5000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    other_income=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    retained_earnings=pd.Series(
        [9989233805.62447, 11109417949.613754],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_equity=pd.Series(
        [9994233805.62447, 11114417949.613754],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [29517397489.168064, 32840357008.766422],
        index=FCST_STOCKROW_MAR_A_INDEX
    ),
)
