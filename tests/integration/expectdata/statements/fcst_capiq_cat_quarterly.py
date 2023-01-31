import pandas as pd

FCST_CAPIQ_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_CAPIQ_CAT_Q_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_Q_INDEX_str]
FCST_CAPIQ_CAT_Q_INDEX_DATA_DICT = dict(
    revenue=pd.Series(
        [12665.637973593799, 12573.944605591882],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Revenue",
    ),
    cogs=pd.Series(
        [8623.604838715046, 8539.911120542369],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Cost of Goods Sold",
    ),
    gross_profit=pd.Series(
        [4042.033134878753, 4034.033485049513],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Gross Profit",
    ),
    rd_exp=pd.Series(
        [468.660042251532, 407.92869769336176],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="R&D Expense",
    ),
    sga=pd.Series(
        [1059.5111357093342, 1055.0412092970707],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="SG&A Expense",
    ),
    dep_exp=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Depreciation & Amortization Expense",
    ),
    other_op_exp=pd.Series(
        [34.193548387096776, 34.193548387096776],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Operating Expenses",
    ),
    op_exp=pd.Series(
        [1562.364726347963, 1497.1634553775293],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Operating Expense",
    ),
    ebit=pd.Series(
        [2479.66840853079, 2536.8700296719835],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Earnings Before Interest and Taxes",
    ),
    int_exp=pd.Series(
        [30.142411426891886, 30.22270023171552],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Interest Expense",
    ),
    gain_on_sale_invest=pd.Series(
        [16.387096774193548, 16.387096774193548],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Gain on Sale of Investments",
    ),
    gain_on_sale_asset=pd.Series(
        [8.96774193548387, 8.96774193548387],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Gain on Sale of Assets",
    ),
    impairment=pd.Series(
        [37.903225806451616, 37.903225806451616],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Impairment Expense",
    ),
    ebt=pd.Series(
        [2449.525997103898, 2506.647329440268],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Earnings Before Tax",
    ),
    tax_exp=pd.Series(
        [814.4958571404948, 833.4893638831567],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Income Tax Expense",
    ),
    net_income=pd.Series(
        [1635.0301399634036, 1673.1579655571115],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Net Income",
    ),
    cash=pd.Series(
        [26446.33897846121, 26922.746140585517],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Cash and Cash Equivalents",
    ),
    st_invest=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Short-Term Investments",
    ),
    cash_and_st_invest=pd.Series(
        [26446.33897846121, 26922.746140585517],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Cash and Short-Term Investments",
    ),
    receivables=pd.Series(
        [7751.895452220302, 7695.775310156022],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Receivables",
    ),
    inventory=pd.Series(
        [10590.372857577071, 10437.773555413978],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Inventory",
    ),
    def_tax_st=pd.Series(
        [710.1935483870968, 710.1935483870968],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Deferred Tax Assets, Current",
    ),
    other_current_assets=pd.Series(
        [49.483870967741936, 49.483870967741936],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Current Assets",
    ),
    total_current_assets=pd.Series(
        [45548.28470761342, 45815.97242551036],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Current Assets",
    ),
    gross_ppe=pd.Series(
        [7034.064516129032, 7034.064516129032],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Gross Property, Plant & Equipment",
    ),
    dep=pd.Series(
        [3509.7419354838707, 3509.7419354838707],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Accumulated Depreciation",
    ),
    net_ppe=pd.Series(
        [3524.3225806451615, 3524.3225806451615],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Net Property, Plant & Equipment",
    ),
    goodwill=pd.Series(
        [6576.741935483871, 6576.741935483871],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Goodwill and Intangible Assets",
    ),
    lt_invest=pd.Series(
        [1328.0, 1328.0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Long-Term Investments",
    ),
    def_tax_lt=pd.Series(
        [1233.6582090644965, 1213.6463929762529],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Deferred Tax Assets, Long-Term",
    ),
    other_lt_assets=pd.Series(
        [964.4193548387096, 964.4193548387096],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Long-Term Assets",
    ),
    total_non_current_assets=pd.Series(
        [13627.14208003224, 13607.130263943996],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Non-Current Assets",
    ),
    total_assets=pd.Series(
        [59175.42678764566, 59423.102689454354],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Assets",
    ),
    payables=pd.Series(
        [6517.281025762845, 6488.128122335316],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Payables",
    ),
    st_debt=pd.Series(
        [0.0, 0.0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Short-Term Debt",
    ),
    current_lt_debt=pd.Series(
        [117.45470136125005, 117.76755946207207],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Current Portion of Long-Term Debt",
    ),
    tax_liab_st=pd.Series(
        [43.38709677419355, 43.38709677419355],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Tax Liabilities, Short-Term",
    ),
    other_current_liab=pd.Series(
        [3833.6129032258063, 3833.6129032258063],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Current Liabilities",
    ),
    total_current_liab=pd.Series(
        [10511.735727124094, 10482.895681797389],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Current Liabilities",
    ),
    lt_debt=pd.Series(
        [9158.329770198974, 9182.724346366625],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Long-Term Debt",
    ),
    total_debt=pd.Series(
        [9158.329770198974, 9182.724346366625],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Debt",
    ),
    deferred_rev=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Deferred Revenue",
    ),
    tax_liab_lt=pd.Series(
        [43.38709677419355, 43.38709677419355],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Tax Liabilities, Long-Term",
    ),
    deposit_liab=pd.Series(
        [0, 0],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Deposit Liabilities",
    ),
    other_lt_liab=pd.Series(
        [3211.548387096774, 3211.548387096774],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Long-Term Liabilities",
    ),
    total_non_current_liab=pd.Series(
        [12413.265254069942, 12437.659830237593],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Non-Current Liabilities",
    ),
    total_liab=pd.Series(
        [22925.000981194036, 22920.55551203498],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Liabilities",
    ),
    common_stock=pd.Series(
        [5982.503225806455, 6034.631451612906],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Common Stock",
    ),
    other_income=pd.Series(
        [-303.7741935483891, -96.66129032258232],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Other Comprehensive Income",
    ),
    retained_earnings=pd.Series(
        [30494.95483870969, 30487.835080645174],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Retained Earnings",
    ),
    minority_interest=pd.Series(
        [76.74193548387096, 76.74193548387096],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Minority Interest",
    ),
    total_equity=pd.Series(
        [36250.425806451625, 36502.54717741937],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Stockholder's Equity",
    ),
    total_liab_and_equity=pd.Series(
        [59175.42678764566, 59423.102689454354],
        index=FCST_CAPIQ_CAT_Q_INDEX,
        name="Total Liabilities and Equity",
    ),
)
