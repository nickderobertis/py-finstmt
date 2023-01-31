import pandas as pd

FCST_STOCKROW_MAR_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_MAR_A_INDEX = [
    pd.to_datetime(val) for val in FCST_STOCKROW_MAR_A_INDEX_str
]
FCST_STOCKROW_MAR_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [20256466666.66667, 21313769696.969704],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Revenue",
    ),
    cogs=pd.Series(
        [16173270221.70731, 16774265514.320612],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [4083196444.959362, 4539504182.649092],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [835333333.3333336, 853230303.0303032],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [835333333.3333336, 853230303.0303032],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [3247863111.6260285, 3686273879.6187887],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [3247863111.6260285, 3686273879.6187887],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [995951943.8210498, 1130389893.195052],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [2251911167.804979, 2555883986.423737],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [6280581868.665095, 9373795939.928816],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [6280581868.665095, 9373795939.928816],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [2142889058.5516183, 2321276679.3028393],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [184800000.0, 184800000.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [8608270927.216717, 11879872619.231655],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [2028093740.9345036, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [0.0, 2102844694.2830825],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [2028093740.9345036, 2102844694.2830825],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [17419000000.0, 17419000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [732000000.0, 732000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [143032821.016846, 119639695.25167897],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [587000000.0, 587000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [20909126561.951347, 20960484389.53476],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [29517397489.168064, 32840357008.766415],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [502163717.91233855, 462537036.8423517],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [776110714.1783538, 887214695.3089361],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [2738275255.3015585, 2964868079.793126],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [4016549687.392251, 4314619811.944414],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [9732820044.698416, 11126120040.225891],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [9732820044.698416, 11126120040.225891],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [5773793951.4529295, 6285199206.98236],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [15506613996.151344, 17411319247.208252],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [19523163683.543594, 21725939059.152664],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [5000000.0, 5000000.0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [9989233805.62447, 11109417949.613754],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [9994233805.62447, 11114417949.613754],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [29517397489.168064, 32840357008.76642],
        index=FCST_STOCKROW_MAR_A_INDEX,
        name="Total Liabilities and Equity",
    ),
)
