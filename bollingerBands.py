# Bollinger Bands for Pair Trading

import numpy as np
import matplotlib.pyplot as plt

def bollinger_bands(data):
    '''
    Calculates the simple moving average (SMA) and Bollinger bands for data array
    :param data: array of observed data (first 20 values are only used to calculate the
    SMA and Bollinger bands for the 21st and onwards points)
    :return: tuple of three numpy arrays containing the sma, the upper Bollinger band
    value, and the lower bollinger value for each time step after the first 20 data points
    '''
    sma = np.zeros(len(data))
    upper_band = np.zeros(len(data))
    lower_band = np.zeros(len(data))

    for i in range(20, len(data)):                          # first 20 values are just used as historical data
        # Simple Moving Average of previous 20 period
        sma[i] = data.iloc[i-20:i].mean()

        # Standard Deviation of previous 20 period
        sd = data.iloc[i-20:i].std()

        # Upper and Lower Bollinger Bands
        upper_band[i] = sma[i] + 2 * sd
        lower_band[i] = sma[i] - 2 * sd
    return sma, upper_band, lower_band

def plot_bollinger_bands(data):
    sma, upper_band, lower_band = bollinger_bands(data)
    data_trimd = data[20:]

    plt.plot(data_trimd.index, data_trimd.values, label='Observed Data', color='k')

    plt.plot(data_trimd.index, sma[20:], label='SMA', color='r')

    plt.plot(data_trimd.index, upper_band[20:], label='Upper Bollinger Band', color='b')
    plt.plot(data_trimd.index, lower_band[20:], label='Lower Bollinger Band', color='b')
    plt.fill_between(data_trimd.index, upper_band[20:], lower_band[20:], alpha=0.3)

    plt.title('Stock Prices with Bollinger Bands')
    plt.xlabel('Date')
    plt.ylabel('Price Ratio')
    plt.legend()
    plt.show()