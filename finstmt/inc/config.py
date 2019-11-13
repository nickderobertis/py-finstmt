
# TODO: use regex instead of names list

# Key is attribute of IncomeStatementData, value is list of possible names to look up from df for that attribute
# Note that each possible name must be unique, it cannot be included in multiple lists
# Also note that all incoming names will be converted to lower case and stripped of punctuation,
# then split on _ and joined with space before matching these names
ALLOWED_NAMES = {
    'revenue': [
        'revenue',
        'rev',
        'sales',
        'sale'
    ],
    'cogs': [
        'cost of revenue',
        'cost of goods sold',
        'cogs',
        'cor'
    ],
    'rd_exp': [
        'rd expenses',
        'rd expense',
        'rd exp',
        'rd',
        'research and development expenses',
        'research and development expense',
        'research and development exp',
        'research and development',
    ],
    'sga': [
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
    'int_exp': [
        'int',
        'int expense',
        'int expenses',
        'int exp',
        'interest',
        'interest expense',
        'interest expenses',
        'interest exp',
    ],
    'tax_exp': [
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
    'op_exp': [
        'op expense',
        'op expenses',
        'op exp',
        'operating expense',
        'operating expenses',
        'operating exp',
    ],
}