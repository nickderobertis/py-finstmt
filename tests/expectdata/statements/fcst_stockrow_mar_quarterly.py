import pandas as pd

FCST_STOCKROW_MAR_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_STOCKROW_MAR_Q_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_MAR_Q_INDEX_str]
FCST_STOCKROW_MAR_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [5249457692.307693, 5319570262.6641655],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    cogs=pd.Series(
        [4269560373.1805205, 4316609326.085905],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    gross_profit=pd.Series(
        [979897319.127172, 1002960936.5782604],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    rd_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    sga=pd.Series(
        [219153846.15384614, 220657692.3076923],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    op_exp=pd.Series(
        [219153846.15384614, 220657692.3076923],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    ebit=pd.Series(
        [760743472.9733258, 782303244.2705681],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    int_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    ebt=pd.Series(
        [760743472.9733258, 782303244.2705681],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    tax_exp=pd.Series(
        [219134872.94473207, 225345242.02680022],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    net_income=pd.Series(
        [541608600.0285938, 556958002.243768],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    cash=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    st_invest=pd.Series(
        [7097693118.813196, 8006310403.303988],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    cash_and_st_invest=pd.Series(
        [7097693118.813196, 8006310403.303988],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    receivables=pd.Series(
        [2414468965.232413, 2483874149.4009943],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    inventory=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_current_assets=pd.Series(
        [143075000.0, 143075000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_current_assets=pd.Series(
        [9655237084.045609, 10633259552.704983],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    gross_ppe=pd.Series(
        [1977916919.1774583, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    dep=pd.Series(
        [0.0, 1995997622.0247183],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    net_ppe=pd.Series(
        [1977916919.1774583, 1995997622.0247183],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    goodwill=pd.Series(
        [17540000000.0, 17540000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    lt_invest=pd.Series(
        [580000000.0, 580000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    def_tax_lt=pd.Series(
        [161573029.44173843, 154472448.77503476],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_lt_assets=pd.Series(
        [1554000000.0, 1554000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_non_current_assets=pd.Series(
        [21813489948.619198, 21824470070.799755],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_assets=pd.Series(
        [31468727032.664806, 32457729623.504738],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    payables=pd.Series(
        [702484420.5215065, 703108761.6099131],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    st_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    current_lt_debt=pd.Series(
        [992388829.6683247, 1033704580.2242877],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_current_liab=pd.Series(
        [2220731611.8502345, 2257047547.767021],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_current_liab=pd.Series(
        [3915604862.040066, 3993860889.6012216],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    lt_debt=pd.Series(
        [11895444560.885262, 12390683126.190437],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_debt=pd.Series(
        [11895444560.885262, 12390683126.190437],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_lt_liab=pd.Series(
        [5859991429.560351, 5997118329.465731],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_non_current_liab=pd.Series(
        [17755435990.445614, 18387801455.656166],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_liab=pd.Series(
        [21671040852.48568, 22381662345.25739],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    common_stock=pd.Series(
        [5000000.0, 5000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    other_income=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    retained_earnings=pd.Series(
        [9792686180.179125, 10071067278.247345],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_equity=pd.Series(
        [9797686180.179125, 10076067278.247345],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
    total_liab_and_equity=pd.Series(
        [31468727032.664803, 32457729623.504734],
        index=FCST_STOCKROW_MAR_Q_INDEX
    ),
)
