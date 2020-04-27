import pandas as pd

FCST_STOCKROW_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_CAT_A_INDEX_str]
FCST_STOCKROW_CAT_NO_BALANCE_A_INDEX_DATA_DICT = dict(
	revenue=pd.Series(
		[57667220437.771454, 60770957074.275894],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	cogs=pd.Series(
		[40454639058.1682, 42291653260.5025],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	gross_profit=pd.Series(
		[17212581379.6033, 18479303813.7734],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	rd_exp=pd.Series(
		[2130500387.0127878, 1973828594.9246898],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	sga=pd.Series(
		[5705772840.60267, 5943016376.151709],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	dep_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_op_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	op_exp=pd.Series(
		[7836273227.61546, 7916844971.07640],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	ebit=pd.Series(
		[9376308151.98783, 10562458842.6970],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	int_exp=pd.Series(
		[465174147.1845381, 471960192.16392887],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	gain_on_sale_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	gain_on_sale_asset=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	impairment=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	ebt=pd.Series(
		[8911134004.803291, 10090498650.533072],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	tax_exp=pd.Series(
		[4078042502.0455694, 4617760471.509786],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	net_income=pd.Series(
		[4833091502.757722, 5472738179.023286],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	cash=pd.Series(
		[8828000000.000004, 9339018181.818186],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	st_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	cash_and_st_invest=pd.Series(
		[8828000000.00000, 9339018181.81819],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	receivables=pd.Series(
		[36913288131.6947, 38900016881.2070],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	inventory=pd.Series(
		[12560519689.0987, 13203297991.0890],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	def_tax_st=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_current_assets=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_current_assets=pd.Series(
		[58301807820.7934, 61442333054.1142],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	gross_ppe=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	dep=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	net_ppe=pd.Series(
		[0, 0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	goodwill=pd.Series(
		[8311100000.0, 8311100000.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	lt_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	def_tax_lt=pd.Series(
		[1301450391.2211661, 1177048728.846231],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_lt_assets=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_non_current_assets=pd.Series(
		[9612550391.22117, 9488148728.84623],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_assets=pd.Series(
		[67914358212.0146, 70930481782.9605],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	payables=pd.Series(
		[7504926219.83506, 8018535007.40337],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	st_debt=pd.Series(
		[11746812154.417807, 11943913393.304642],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	current_lt_debt=pd.Series(
		[0, 0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	tax_liab_st=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_current_liab=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_current_liab=pd.Series(
		[19251738374.25287, 19962448400.708008],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	lt_debt=pd.Series(
		[25339312566.232864, 25683230453.16987],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_debt=pd.Series(
		[37086124720.65067, 37627143846.47451],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	deferred_rev=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	tax_liab_lt=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	deposit_liab=pd.Series(
		[1721200000.0, 1721200000.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_lt_liab=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_non_current_liab=pd.Series(
		[27060512566.2329, 27404430453.1699],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_liab=pd.Series(
		[46312250940.48573, 47366878853.87788],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	common_stock=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	other_income=pd.Series(
		[-1553858022.6100283, -1433773607.1434367],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	retained_earnings=pd.Series(
		[32254733333.333347, 33119884848.484863],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	minority_interest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_equity=pd.Series(
		[30700875310.7233, 31686111241.3414],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
	total_liab_and_equity=pd.Series(
		[77013126251.20905, 79052990095.2193],
		index=FCST_STOCKROW_CAT_A_INDEX
	),
)
