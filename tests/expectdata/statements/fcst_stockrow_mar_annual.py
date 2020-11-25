import pandas as pd

FCST_STOCKROW_MAR_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_STOCKROW_MAR_A_INDEX = [pd.to_datetime(val) for val in FCST_STOCKROW_MAR_A_INDEX_str]
FCST_STOCKROW_MAR_A_INDEX_DATA_DICT = dict(
	revenue=pd.Series(
		[20256466666.666676, 21313769696.969707],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	cogs=pd.Series(
		[16173270221.707317, 16774265514.320618],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	gross_profit=pd.Series(
		[4083196444.959358, 4539504182.64909],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	rd_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	sga=pd.Series(
		[835333333.3333337, 853230303.0303035],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	dep_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_op_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	op_exp=pd.Series(
		[835333333.3333337, 853230303.0303035],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	ebit=pd.Series(
		[3247863111.6260242, 3686273879.6187863],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	int_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	gain_on_sale_invest=pd.Series(
		[-0.0, -0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	gain_on_sale_asset=pd.Series(
		[-0.0, -0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	impairment=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	ebt=pd.Series(
		[3247863111.6260242, 3686273879.6187863],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	tax_exp=pd.Series(
		[995951943.8210485, 1130389893.1950512],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	net_income=pd.Series(
		[2251911167.8049755, 2555883986.423735],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	cash=pd.Series(
		[0.0, 4704119695.038036],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	st_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	cash_and_st_invest=pd.Series(
		[0.0, 4704119695.038036],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	receivables=pd.Series(
		[2142889058.5516188, 2321276679.3028398],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	inventory=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	def_tax_st=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_current_assets=pd.Series(
		[184800000.0, 184800000.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_current_assets=pd.Series(
		[2327689058.5516186, 7210196374.340876],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	gross_ppe=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	dep=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	net_ppe=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	goodwill=pd.Series(
		[17419000000.0, 17419000000.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	lt_invest=pd.Series(
		[732000000.0, 732000000.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	def_tax_lt=pd.Series(
		[143032821.016846, 119639695.25167897],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_lt_assets=pd.Series(
		[587000000.0, 587000000.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_non_current_assets=pd.Series(
		[18881032821.016846, 18857639695.25168],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_assets=pd.Series(
		[21208721879.568466, 26067836069.592556],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	payables=pd.Series(
		[502163717.91233873, 462537036.84235173],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	st_debt=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	current_lt_debt=pd.Series(
		[776110714.178354, 387047173.9166403],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	tax_liab_st=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_current_liab=pd.Series(
		[2738275255.3015585, 2964868079.793126],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_current_liab=pd.Series(
		[4016549687.392251, 3814452290.5521183],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	lt_debt=pd.Series(
		[9732820044.698414, 4853766896.553964],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_debt=pd.Series(
		[9732820044.698414, 4853766896.553964],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	deferred_rev=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	tax_liab_lt=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	deposit_liab=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_lt_liab=pd.Series(
		[5773793951.4529295, 6285199206.98236],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_non_current_liab=pd.Series(
		[15506613996.151344, 11138966103.536324],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_liab=pd.Series(
		[19523163683.543594, 14953418394.088442],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	common_stock=pd.Series(
		[5000000.0, 5000000.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	other_income=pd.Series(
		[-0.0, -0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	retained_earnings=pd.Series(
		[9989233805.62447, 11109417949.613754],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	minority_interest=pd.Series(
		[0.0, 0.0],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_equity=pd.Series(
		[9994233805.62447, 11114417949.613754],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
	total_liab_and_equity=pd.Series(
		[29517397489.168064, 26067836343.702194],
		index=FCST_STOCKROW_MAR_A_INDEX
	),
)
