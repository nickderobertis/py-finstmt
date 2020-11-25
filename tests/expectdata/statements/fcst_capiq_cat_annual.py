import pandas as pd

FCST_CAPIQ_CAT_A_INDEX_str = ["2019-12-31 00:00:00", "2020-12-31 00:00:00"]
FCST_CAPIQ_CAT_A_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_A_INDEX_str]
FCST_CAPIQ_CAT_A_INDEX_DATA_DICT = dict(
	revenue=pd.Series(
		[54630.06518336638, 54538.284820343906],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	cogs=pd.Series(
		[36258.93669756555, 35382.62984773562],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	gross_profit=pd.Series(
		[18371.12848580083, 19155.65497260829],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	rd_exp=pd.Series(
		[1660.4438910269068, 1348.95936412214],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	sga=pd.Series(
		[4613.797118402208, 4429.280867618918],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	dep_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_op_exp=pd.Series(
		[51.4, 51.4],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	op_exp=pd.Series(
		[6325.641009429115, 5829.6402317410575],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	ebit=pd.Series(
		[12045.487476371714, 13326.014740867231],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	int_exp=pd.Series(
		[94.76554690770675, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	gain_on_sale_invest=pd.Series(
		[83.4, 83.4],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	gain_on_sale_asset=pd.Series(
		[-0.0, -0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	impairment=pd.Series(
		[119.0, 119.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	ebt=pd.Series(
		[11950.721929464007, 13326.014740867231],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	tax_exp=pd.Series(
		[7075.201613807044, 7889.418024843036],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	net_income=pd.Series(
		[4875.520315656963, 5436.596716024195],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	cash=pd.Series(
		[7255.499999999999, 35135.10372958528],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	st_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	cash_and_st_invest=pd.Series(
		[7255.5, 35135.10372958528],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	receivables=pd.Series(
		[8266.894222673915, 8253.005559896765],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	inventory=pd.Series(
		[11708.880980931483, 11651.321876515995],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	def_tax_st=pd.Series(
		[328.8, 328.8],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_current_assets=pd.Series(
		[26.2, 26.2],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_current_assets=pd.Series(
		[27586.275203605397, 55394.43116599804],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	gross_ppe=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	dep=pd.Series(
		[16218.0, 16218.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	net_ppe=pd.Series(
		[16218.0, 16218.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	goodwill=pd.Series(
		[6335.6, 6335.6],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	lt_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	def_tax_lt=pd.Series(
		[1383.055805600257, 1403.4067215000555],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_lt_assets=pd.Series(
		[1168.6, 1168.6],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_non_current_assets=pd.Series(
		[7330.744194399742, 7310.393278499943],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_assets=pd.Series(
		[20255.531009205653, 48084.037887498096],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	payables=pd.Series(
		[7673.534479950695, 7973.837887498099],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	st_debt=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	current_lt_debt=pd.Series(
		[58.95668581440481, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	tax_liab_st=pd.Series(
		[82.8, 82.8],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_current_liab=pd.Series(
		[3499.0, 3499.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_current_liab=pd.Series(
		[11314.291165765098, 11555.637887498098],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	lt_debt=pd.Series(
		[7223.835516037975, 9.094947017729282e-13],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_debt=pd.Series(
		[7223.835516037975, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	deferred_rev=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	tax_liab_lt=pd.Series(
		[82.8, 82.8],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	deposit_liab=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_lt_liab=pd.Series(
		[3236.0, 3236.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_non_current_liab=pd.Series(
		[10542.635516037975, 3318.7999999999993],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_liab=pd.Series(
		[21856.926681803074, 14874.437887498098],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	common_stock=pd.Series(
		[5983.299999999999, 6181.0],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	other_income=pd.Series(
		[424.90000000000055, 1458.6000000000004],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	retained_earnings=pd.Series(
		[26488.099999999995, 25501.6],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	minority_interest=pd.Series(
		[68.4, 68.4],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_equity=pd.Series(
		[32964.7, 33209.6],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
	total_liab_and_equity=pd.Series(
		[54821.62668180307, 48084.037887498096],
		index=FCST_CAPIQ_CAT_A_INDEX
	),
)
