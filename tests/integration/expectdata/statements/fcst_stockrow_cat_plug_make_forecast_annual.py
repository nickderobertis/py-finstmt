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
        name="Revenue",
    ),
    cogs=pd.Series(
        [40454639058.16816, 42291653260.50249],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [17212581379.603294, 18479303813.773407],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [2130504180.795485, 1973832561.7877598],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [5705772840.60267, 5943016376.151709],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [7836277021.398155, 7916848937.939468],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [9376304358.20514, 10562454875.833939],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [598429523.6351756, 1073345677.2586178],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [8777874834.569963, 9489109198.575321],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [3258650120.395457, 3522684865.658374],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [5519224714.174506, 5966424332.916947],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [8828000000.000004, 9339018181.818184],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [8828000000.000004, 9339018181.818184],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [36913288131.6947, 38900016881.20703],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [12560519689.098722, 13203297991.089027],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [58301807820.79343, 61442333054.11424],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [13698894523.433386, 0.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [0.0, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [13698894523.433386, 13824938202.751822],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [8311100000.0, 8311100000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [7195000000.0, 43170000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [29204994523.433388, 65306038202.75182],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [87506802344.2268, 126748371256.86606],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [7504926219.835061, 8018535007.403371],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [22370630224.82553, 59889520947.807976],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [29875556444.66059, 67908055955.21135],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [25339312566.232864, 25683230453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [47709942791.058395, 85572751400.97784],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [1721200000.0, 1721200000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [27060512566.232864, 27404430453.16987],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [56936069010.89346, 95312486408.38123],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [-1684000000.0, -1684000000.0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [32254733333.333344, 33119884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [30570733333.333344, 31435884848.484863],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [87506802344.2268, 126748371256.86609],
        index=FCST_STOCKROW_CAT_PLUG_MAKE_FORECAST_A_INDEX,
        name="Total Liabilities and Equity",
    ),
)
