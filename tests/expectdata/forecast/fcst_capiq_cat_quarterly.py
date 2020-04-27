import pandas as pd

FCST_CAPIQ_CAT_Q_INDEX_str = ["2019-12-31 00:00:00", "2020-03-31 00:00:00"]
FCST_CAPIQ_CAT_Q_INDEX = [pd.to_datetime(val) for val in FCST_CAPIQ_CAT_Q_INDEX_str]
FCST_CAPIQ_CAT_Q_INDEX_DATA_DICT = dict(
	revenue=pd.Series(
		[12665.637973593799, 12573.944605591882],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	cogs=pd.Series(
		[8623.604838715039, 8539.911120542363],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	gross_profit=pd.Series(
		[4042.0331348787604, 4034.0334850495183],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	rd_exp=pd.Series(
		[468.6580155707379, 407.9238199871619],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	sga=pd.Series(
		[1059.5111357093342, 1055.0412092970707],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	dep_exp=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_op_exp=pd.Series(
		[34.193548387096776, 34.193548387096776],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	op_exp=pd.Series(
		[1562.362699667169, 1497.1585776713293],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	ebit=pd.Series(
		[2479.670435211591, 2536.874907378189],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	int_exp=pd.Series(
		[30.14241142689188, 7.105427357601002e-15],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	gain_on_sale_invest=pd.Series(
		[16.387096774193548, 16.387096774193548],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	gain_on_sale_asset=pd.Series(
		[8.96774193548387, 8.96774193548387],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	impairment=pd.Series(
		[37.903225806451616, 37.903225806451616],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	ebt=pd.Series(
		[2449.5280237846996, 2536.874907378189],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	tax_exp=pd.Series(
		[814.4965310354108, 843.5403847871752],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	net_income=pd.Series(
		[1635.0314927492886, 1693.3345225910139],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	cash=pd.Series(
		[8024.038709677421, 17238.712755777484],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	st_invest=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	cash_and_st_invest=pd.Series(
		[8024.038709677421, 17238.712755777484],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	receivables=pd.Series(
		[7751.895452220302, 7695.775310156022],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	inventory=pd.Series(
		[10590.372857577066, 10437.773555413973],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	def_tax_st=pd.Series(
		[710.1935483870968, 710.1935483870968],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_current_assets=pd.Series(
		[49.483870967741936, 49.483870967741936],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_current_assets=pd.Series(
		[27125.984438829626, 36131.93904070232],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	gross_ppe=pd.Series(
		[7034.064516129032, 7034.064516129032],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	dep=pd.Series(
		[3509.7419354838707, 3509.7419354838707],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	net_ppe=pd.Series(
		[3524.3225806451615, 3524.3225806451615],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	goodwill=pd.Series(
		[6576.741935483871, 6576.741935483871],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	lt_invest=pd.Series(
		[1328.0, 1328.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	def_tax_lt=pd.Series(
		[1233.6582090644965, 1213.6463929762529],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_lt_assets=pd.Series(
		[964.4193548387096, 964.4193548387096],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_non_current_assets=pd.Series(
		[13627.14208003224, 13607.130263943996],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_assets=pd.Series(
		[40753.12651886186, 49739.06930464631],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	payables=pd.Series(
		[6517.281025762843, 6488.1281223353135],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	st_debt=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	current_lt_debt=pd.Series(
		[117.45470136125009, 2.3328364727372695e-14],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	tax_liab_st=pd.Series(
		[43.38709677419355, 43.38709677419355],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_current_liab=pd.Series(
		[3833.6129032258063, 3833.6129032258063],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_current_liab=pd.Series(
		[10511.735727124093, 10365.128122335313],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	lt_debt=pd.Series(
		[9158.329770198972, 1.8189894035458565e-12],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_debt=pd.Series(
		[9158.329770198972, 1.8189894035458565e-12],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	deferred_rev=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	tax_liab_lt=pd.Series(
		[43.38709677419355, 43.38709677419355],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	deposit_liab=pd.Series(
		[0.0, 0.0],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_lt_liab=pd.Series(
		[3211.548387096774, 3211.548387096774],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_non_current_liab=pd.Series(
		[12413.26525406994, 3254.9354838709696],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_liab=pd.Series(
		[22925.000981194033, 13620.063606206282],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	common_stock=pd.Series(
		[5982.503225806452, 6034.631451612904],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	other_income=pd.Series(
		[-303.77419354839003, -96.66129032258323],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	retained_earnings=pd.Series(
		[30494.954838709687, 30487.83508064517],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	minority_interest=pd.Series(
		[76.74193548387096, 76.74193548387096],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_equity=pd.Series(
		[36250.42580645162, 36502.547177419365],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
	total_liab_and_equity=pd.Series(
		[59175.42678764565, 50122.61078362565],
		index=FCST_CAPIQ_CAT_Q_INDEX
	),
)
