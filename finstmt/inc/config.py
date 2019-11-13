from finstmt.items.config import ItemConfig

# TODO: use regex instead of names list

# Note that each possible extract_name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
INCOME_STATEMENT_INPUT_ITEMS = [
    ItemConfig(
        'revenue',
        'Revenue',
        extract_names=[
            'revenue',
            'rev',
            'sales',
            'sale'
        ],
    ),
    ItemConfig(
        'cogs',
        'Cost of Goods Sold',
        extract_names=[
            'cost of revenue',
            'cost of goods sold',
            'cogs',
            'cor'
        ],
    ),
    ItemConfig(
        'op_exp',
        'Operating Expense',
        extract_names=[
            'op expense',
            'op expenses',
            'op exp',
            'operating expense',
            'operating expenses',
            'operating exp',
        ],
    ),
    ItemConfig(
        'gross_profit',
        'Gross Profit',
    ),
    ItemConfig(
        'rd_exp',
        'R&D Expense',
        extract_names=[
            'rd expenses',
            'rd expense',
            'rd exp',
            'rd',
            'research and development expenses',
            'research and development expense',
            'research and development exp',
            'research and development',
        ],
    ),
    ItemConfig(
        'sga',
        'SG&A Expense',
         extract_names=[
            'sga',
            'sga expense',
            'sga expenses',
            'sga exp',
            'selling general and administrative',
            'selling general and administrative expense',
            'selling general and administrative expenses',
            'selling general and administrative exp',
            'selling general administrative',
            'selling general administrative expense',
            'selling general administrative expenses',
            'selling general administrative exp',
        ],
    ),
    ItemConfig(
        'ebit',
        'Earnings Before Interest and Taxes',
    ),
    ItemConfig(
        'int_exp',
        'Interest Expense',
        extract_names=[
            'int',
            'int expense',
            'int expenses',
            'int exp',
            'interest',
            'interest expense',
            'interest expenses',
            'interest exp',
        ],
    ),
    ItemConfig(
        'ebt',
        'Earnings Before Tax',
    ),
    ItemConfig(
        'tax_exp',
        'Income Tax Expense',
        extract_names=[
            'taxes',
            'tax',
            'tax expense',
            'tax expenses',
            'tax exp',
            'income tax',
            'income tax expense',
            'income tax expenses',
            'income tax exp',
        ],
    ),
    ItemConfig(
        'net_income',
        'Net Income',
    ),
]