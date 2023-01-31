import pandas as pd

FCST_CAPIQ_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_CAPIQ_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_A_INDEX_str]
FCST_CAPIQ_CAT_A_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [54630.06518336638, 54538.284820343906],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Revenue",
    ),
    cogs=pd.Series(
        [36258.93669756556, 35382.62984773563],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [18371.128485800822, 19155.654972608274],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [1660.4874275857828, 1349.0032098336733],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [4613.797118402208, 4429.280867618918],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [51.4, 51.4],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [6325.684545987991, 5829.684077452592],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [12045.44393981283, 13325.970895155682],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [94.76554690770675, 90.68363007665357],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [83.4, 83.4],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [119.0, 119.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [11950.678392905123, 13235.287265079029],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [7075.175838800857, 7835.7045180856985],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [4875.502554104267, 5399.58274699333],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [10459.995672597433, 10742.59804190024],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [10459.995672597433, 10742.59804190024],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [8266.894222673915, 8253.005559896765],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [11708.880980931483, 11651.321876515996],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [328.8, 328.8],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [26.2, 26.2],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [30790.77087620283, 31001.925478313],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [31361.6, 31361.6],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [16218.0, 16218.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [15143.599999999999, 15143.599999999999],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [6335.6, 6335.6],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [1383.055805600257, 1403.4067215000555],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [1168.6, 1168.6],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [24030.855805600255, 24051.206721500053],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [54821.626681803085, 55053.13219981306],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [7673.534479950697, 7973.8378874981],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [0.0, 0.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [58.95668581440259, 56.41719444879978],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [82.8, 82.8],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [3499.0, 3499.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [11314.291165765098, 11612.055081946897],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [7223.835516037974, 6912.6771178661575],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [7223.835516037974, 6912.6771178661575],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [82.8, 82.8],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [3236.0, 3236.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [10542.635516037975, 10231.477117866158],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [21856.926681803074, 21843.532199813053],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [5983.3, 6181.0],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [424.90000000000146, 1458.6000000000022],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [26488.100000000002, 25501.600000000006],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [68.4, 68.4],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [32964.700000000004, 33209.600000000006],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [54821.62668180308, 55053.13219981306],
        index=FCST_CAPIQ_CAT_A_INDEX,
        name="Total Liabilities and Equity",
    ),
)
