import pandas as pd


STOCKROW_FCST_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
STOCKROW_FCST_CAT_A_INDEX = [pd.to_datetime(val) for val in STOCKROW_FCST_CAT_A_INDEX_str]
STOCKROW_FCST_CAT_A_INDEX_DATA_DICT = dict(
        revenue=pd.Series(
                [57667220437.771454, 60770957074.275894],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        cogs=pd.Series(
                [40454639058.16817, 42291653260.502495],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        gross_profit=pd.Series(
                [17212581379.603287, 18479303813.7734],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        rd_exp=pd.Series(
                [2130500387.0127878, 1973828594.9246898],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        sga=pd.Series(
                [5705772840.60267, 5943016376.151709],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        dep_exp=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_op_exp=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        op_exp=pd.Series(
                [7836273227.615458, 7916844971.076399],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        ebit=pd.Series(
                [9376308151.98783, 10562458842.697],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        int_exp=pd.Series(
                [465174147.1845398, 396638121.6220207],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        gain_on_sale_invest=pd.Series(
                [-0.0, -0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        gain_on_sale_asset=pd.Series(
                [-0.0, -0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        impairment=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        ebt=pd.Series(
                [8911134004.80329, 10165820721.07498],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        tax_exp=pd.Series(
                [4078042502.0455675, 4652230450.846467],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        net_income=pd.Series(
                [4833091502.757722, 5513590270.228513],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        cash=pd.Series(
                [8828000000.000004, 11456455645.302628],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        st_invest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        cash_and_st_invest=pd.Series(
                [8828000000.000004, 11456455645.302628],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        receivables=pd.Series(
                [36913288131.6947, 38900016881.20703],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        inventory=pd.Series(
                [12560519689.09872, 13203297991.089025],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        def_tax_st=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_current_assets=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_current_assets=pd.Series(
                [58301807820.79343, 63559770517.59869],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        gross_ppe=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        dep=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        net_ppe=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        goodwill=pd.Series(
                [8311100000.0, 8311100000.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        lt_invest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        def_tax_lt=pd.Series(
                [1301450391.2211661, 1177048728.846231],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_lt_assets=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_non_current_assets=pd.Series(
                [9612550391.221167, 9488148728.846231],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_assets=pd.Series(
                [67914358212.014595, 73047919246.44492],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        payables=pd.Series(
                [7504926219.83506, 8018535007.403367],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        st_debt=pd.Series(
                [11746812154.417807, 10037735071.289598],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        current_lt_debt=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        tax_liab_st=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_current_liab=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_current_liab=pd.Series(
                [19251738374.25287, 18056270078.692966],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        lt_debt=pd.Series(
                [25339312566.232864, 21584337944.740208],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_debt=pd.Series(
                [37086124720.65067, 31622073016.029808],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        deferred_rev=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        tax_liab_lt=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        deposit_liab=pd.Series(
                [1721200000.0, 1721200000.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_lt_liab=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_non_current_liab=pd.Series(
                [27060512566.232864, 23305537944.740208],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_liab=pd.Series(
                [46312250940.48573, 41361808023.433174],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        common_stock=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        other_income=pd.Series(
                [-1553858022.6100283, -1433773607.1434367],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        retained_earnings=pd.Series(
                [32254733333.333347, 33119884848.484863],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        minority_interest=pd.Series(
                [0.0, 0.0],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_equity=pd.Series(
                [30700875310.72332, 31686111241.341427],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
        total_liab_and_equity=pd.Series(
                [77013126251.20905, 73047919264.7746],
                index=STOCKROW_FCST_CAT_A_INDEX
        ),
)
