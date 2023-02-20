from typing import Final, List, TypedDict

from finstmt import FinancialStatements


class AdjustDict(TypedDict, total=False):
    trend: List[str]
    auto: List[str]
    recent: List[str]
    mean: List[str]


class ForecastAdjustDicts(TypedDict):
    capiq: AdjustDict
    stockrow_cat: AdjustDict
    stockrow_mar: AdjustDict


FORECAST_ADJUSTS: Final = ForecastAdjustDicts(
    capiq=AdjustDict(
        trend=[
            "cogs",
            "cash",
            "inventory",
            "payables",
            "common_stock",
            "other_income",
            "retained_earnings",
        ],
        auto=[
            "rd_exp",
        ],
        recent=[
            "lt_invest",
        ],
        mean=[
            # Because zeroes
            "dep_exp",
            "other_op_exp",
            "gain_on_sale_invest",
            "gain_on_sale_asset",
            "impairment",
            "st_invest",
            "def_tax_st",
            "other_current_assets",
            "gross_ppe",
            "dep",
            "other_lt_assets",
            "current_lt_debt",
            "tax_liab_lt",
            "tax_liab_st",
            "other_current_liab",
            "deferred_rev",
            "other_lt_liab",
            "minority_interest",
            # Because flat
            "int_exp",
            "tax_exp",
            "receivables",
            "goodwill",
            "deposit_liab",
        ],
    ),
    stockrow_cat=AdjustDict(
        trend=[
            "cogs",
            "cash",
            "inventory",
            "payables",
            "retained_earnings",
        ],
        auto=[
            "rd_exp",
        ],
        recent=[
            "lt_invest",
        ],
        mean=[
            # Because zeroes
            "dep_exp",
            "other_op_exp",
            "gain_on_sale_invest",
            "gain_on_sale_asset",
            "impairment",
            "st_invest",
            "def_tax_st",
            "other_current_assets",
            "gross_ppe",
            "dep",
            "other_lt_assets",
            "current_lt_debt",
            "tax_liab_lt",
            "tax_liab_st",
            "other_current_liab",
            "deferred_rev",
            "other_lt_liab",
            "common_stock",
            "minority_interest",
            # Because flat
            "int_exp",
            "tax_exp",
            "receivables",
            "goodwill",
            "deposit_liab",
        ],
    ),
    stockrow_mar=AdjustDict(
        trend=[
            "revenue",
            "sga",
            "cogs",
            "cash",
            "payables",
        ],
        auto=[],
        recent=[
            "lt_invest",
            "inventory",
            "goodwill",
            "other_lt_assets",
            "deferred_rev",
            "tax_liab_lt",
        ],
        mean=[
            # Because zeroes
            "rd_exp",
            "dep_exp",
            "other_op_exp",
            "gain_on_sale_invest",
            "gain_on_sale_asset",
            "impairment",
            "st_invest",
            "def_tax_st",
            "other_current_assets",
            "gross_ppe",
            "dep",
            "current_lt_debt",
            "tax_liab_st",
            "common_stock",
            "minority_interest",
            # Because flat
            "int_exp",
            "tax_exp",
            "deposit_liab",
        ],
    ),
)


def adjust_forecast_methods(stmts: FinancialStatements, adjust_dict: AdjustDict):
    for method, var_list in adjust_dict.items():
        for var in var_list:
            stmts.config.update(var, ["forecast_config", "method"], method)
