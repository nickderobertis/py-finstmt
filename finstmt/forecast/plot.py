import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

PAD_PCT = 0.2

def plot_forecast(fcst_df: pd.DataFrame, orig_data: np.ndarray, orig_dates: pd.DatetimeIndex) -> plt.Figure:
    fig = plt.figure(facecolor='w', figsize=(10, 5))
    ax = fig.add_subplot(111)
    fcst_t = fcst_df.index.to_pydatetime()
    ax.plot(orig_dates, orig_data, 'k.')
    ax.plot(fcst_t, fcst_df['mean'], ls='-', c='#0072B2')
    ax.fill_between(fcst_t, fcst_df['lower'], fcst_df['upper'],
                    color='#0072B2', alpha=0.2)

    # Set y-range based only on the mean and orig data and not confidence interval as it can get very large
    max_point = max(fcst_df['mean'].max(), orig_data.max())
    min_point = min(fcst_df['mean'].min(), orig_data.min())
    y_lim_upper = max_point * (1 + PAD_PCT)
    y_lim_lower = min_point * (1 - PAD_PCT)
    ax.set_ylim([y_lim_lower, y_lim_upper])

    return fig