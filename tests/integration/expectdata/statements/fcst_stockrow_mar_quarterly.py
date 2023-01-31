import pandas as pd

FCST_STOCKROW_MAR_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_STOCKROW_MAR_Q_INDEX = [
    pd.to_datetime(val) for val in FCST_STOCKROW_MAR_Q_INDEX_str
]
FCST_STOCKROW_MAR_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [5249457692.307693, 5319570262.6641655],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Revenue",
    ),
    cogs=pd.Series(
        [4269560373.1805205, 4316609326.085905],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [979897319.127172, 1002960936.5782604],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [219153846.15384614, 220657692.3076923],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [219153846.15384614, 220657692.3076923],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [760743472.9733258, 782303244.2705681],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [760743472.9733258, 782303244.2705681],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [219134872.94473207, 225345242.02680022],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [541608600.0285938, 556958002.2437679],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [7097693118.813196, 8006310403.30399],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [7097693118.813196, 8006310403.30399],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [2414468965.232413, 2483874149.4009943],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [143075000.0, 143075000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [9655237084.045612, 10633259552.704985],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [1977916919.1774583, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [0.0, 1995997622.0247183],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [1977916919.1774583, 1995997622.0247183],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [17540000000.0, 17540000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [580000000.0, 580000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [161573029.44173843, 154472448.77503476],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [1554000000.0, 1554000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [21813489948.619198, 21824470070.799755],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [31468727032.66481, 32457729623.504738],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [702484420.5215065, 703108761.6099131],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [992388829.668325, 1033704580.224288],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [2220731611.8502345, 2257047547.767021],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [3915604862.0400662, 3993860889.601222],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [11895444560.885265, 12390683126.190437],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [11895444560.885265, 12390683126.190437],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [5859991429.560351, 5997118329.465731],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [17755435990.445618, 18387801455.656166],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [21671040852.485683, 22381662345.25739],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [5000000.0, 5000000.0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [9792686180.179125, 10071067278.247345],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [9797686180.179125, 10076067278.247345],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [31468727032.66481, 32457729623.504734],
        index=FCST_STOCKROW_MAR_Q_INDEX,
        name="Total Liabilities and Equity",
    ),
)
