from finstmt.items.config import ItemConfig

# TODO: use regex instead of names list

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
BALANCE_SHEET_INPUT_ITEMS = [
    ItemConfig(
        'cash',
        'Cash and Cash Equivalents',
        extract_names=[
            'cash',
            'cash and cash equivalents',
            'cash cash equivalents',
            'cash equiv'
        ],
    ),
    ItemConfig(
        'st_invest',
        'Short-Term Investments',
        extract_names=[
            'shortterm investments',
            'short term investments',
            'st investments',
            'shortterm invest',
            'short term invest',
            'st invest',
        ]
    ),
    ItemConfig(
        'cash_and_st_invest',
        'Cash and Short-Term Investments'
    ),
    ItemConfig(
        'receivables',
        'Receivables',
        extract_names=[
            'receivables',
            'rec',
            'accounts receivable',
            'ar'
        ]
    ),
    ItemConfig(
        'inventory',
        'Inventory',
        extract_names=[
            'inv',
            'inventory',
            'inventories'
        ]
    ),
    ItemConfig(
        'total_current_assets',
        'Total Current Assets',
        extract_names=[
            'total current assets',
            'tca',
        ]
    ),
    ItemConfig(
        'ppe',
        'Property, Plant & Equipment',
        extract_names=[
            'ppe',
            'property plant equipment',
            'property plant and equipment',
            'ppe net',
            'property plant equipment net',
            'property plant and equipment net',
        ]
    ),
    ItemConfig(
        'goodwill',
        'Goodwill and Intangible Assets',
        extract_names=[
            'goodwill',
            'goodwill and intangible assets',
            'goodwill and intangibles',
            'goodwill intangible assets',
            'goodwill intangibles',
        ]
    ),
    ItemConfig(
        'lt_invest',
        'Long-Term Investments',
        extract_names=[
            'lt invest',
            'lt investments',
            'long term invest',
            'long term investments',
            'longterm invest',
            'longterm investments',
        ]
    ),
    ItemConfig(
        'tax_assets',
        'Tax Assets',
        extract_names=[
            'tax assets'
        ]
    ),
    ItemConfig(
        'total_non_current_assets',
        'Total Non-Current Assets',
        extract_names=[
            'total non current assets',
            'total noncurrent assets',
        ]
    ),
    ItemConfig(
        'total_assets',
        'Total Assets',
        extract_names=[
            'total assets',
            'total asset'
        ]
    ),
    ItemConfig(
        'payables',
        'Payables',
        extract_names=[
            'payables',
            'accounts payable',
            'ap'
        ]
    ),
    ItemConfig(
        'st_debt',
        'Short-Term Debt',
        extract_names=[
            'st debt',
            'short term debt',
            'shortterm debt'
        ]
    ),
    ItemConfig(
        'total_current_liab',
        'Total Current Liabilities',
        extract_names=[
            'total current liabilities',
        ]
    ),
    ItemConfig(
        'lt_debt',
        'Long-Term Debt',
        extract_names=[
            'lt debt',
            'long term debt',
            'longterm debt'
        ]
    ),
    ItemConfig(
        'total_debt',
        'Total Debt',
        extract_names=[
            'total debt'
        ]
    ),
    ItemConfig(
        'deferred_rev',
        'Deferred Revenue',
        extract_names=[
            'deferred revenue',
            'deferred sales'
        ]
    ),
    ItemConfig(
        'tax_liab',
        'Tax Liabilities',
        extract_names=[
            'tax liab',
            'tax liability',
            'tax liabilities'
        ]
    ),
    ItemConfig(
        'deposit_liab',
        'Deposit Liabilities',
        extract_names=[
            'deposit liab',
            'deposit liability',
            'deposit liabilities',
        ]
    ),
    ItemConfig(
        'total_non_current_liab',
        'Total Non-Current Liabilities',
        extract_names=[
            'total non current liabilities',
            'total noncurrent liabilities',
            'total non current liability',
            'total noncurrent liability',
            'total non current liab',
            'total noncurrent liab',
        ]
    ),
    ItemConfig(
        'total_liab',
        'Total Liabilities',
        extract_names=[
            'total liab',
            'total liability',
            'total liabilities',
        ]
    ),
    ItemConfig(
        'other_income',
        'Other Comprehensive Income',
        extract_names=[
            'other income',
            'other comprehensive income',
            'other comp income',
            'comp income',
            'comprehensive income'
        ]
    ),
    ItemConfig(
        'retained_earnings',
        'Retained Earnings',
        extract_names=[
            're',
            'retained earnings',
            'retained earnings deficit',
            're deficit'
        ]
    ),
    ItemConfig(
        'total_equity',
        "Total Stockholder's Equity",
        extract_names=[
            'total equity',
            'total shareholders equity',
            'total stockholders equity'
        ]
    )
]