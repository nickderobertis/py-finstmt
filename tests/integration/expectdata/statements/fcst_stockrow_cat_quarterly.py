import pandas as pd

FCST_STOCKROW_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_STOCKROW_CAT_Q_INDEX = [
    pd.to_datetime(val) for val in FCST_STOCKROW_CAT_Q_INDEX_str
]
FCST_STOCKROW_CAT_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [12911872667.210337, 13067601173.714796],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Revenue",
    ),
    cogs=pd.Series(
        [9037499726.122707, 9129684386.837864],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [3874372941.0876293, 3937916786.876932],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [556705942.8941139, 476757814.35749084],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [1259904043.8414893, 1268871462.5804458],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [1816609986.7356033, 1745629276.9379365],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [2057762954.352026, 2192287509.9389954],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [117698628.55091406, 118235016.75847101],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [1940064325.801112, 2074052493.1805243],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [592740807.948901, 633677726.1385959],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [1347323517.8522108, 1440374767.0419285],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [11716323534.650227, 11717870550.022476],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [11716323534.650227, 11717870550.022476],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [32121906078.42198, 32509324432.722553],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [11817497605.127018, 11966311963.142387],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [55655727218.19922, 56193506945.88742],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [12853612568.208256, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [0.0, 12865235637.252861],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [12853612568.208256, 12865235637.252861],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [8462500000.0, 8462500000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [0.0, 0.0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [1336374408.7046144, 1301673877.7263904],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [22652486976.912872, 22629409514.97925],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [78308214195.11209, 78822916460.86667],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [6762939214.231989, 6872127631.8362055],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [12389396735.328043, 12461220850.213617],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [19152335949.56003, 19333348482.049824],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [25689310937.85975, 25791022997.578564],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [38078707673.18779, 38252243847.79218],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [1839275000.0, 1839275000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [27528585937.85975, 27630297997.578564],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [46680921887.41978, 46963646479.62839],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [-1783000000.0, -1783000000.0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [33410292307.692314, 33642269981.23828],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [0, 0],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [31627292307.692314, 31859269981.23828],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [78308214195.11209, 78822916460.86667],
        index=FCST_STOCKROW_CAT_Q_INDEX,
        name="Total Liabilities and Equity",
    ),
)
