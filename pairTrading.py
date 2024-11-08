# Simple Pair Trading Strategy with Kalman Filter

import kalmanFilter as kf
import bollingerBands as bb
import matplotlib.pyplot as plt

def plot_pair_prices(dataA, dataB):
    # Plotting observed stock price data pair for checking relation
    plt.plot(dataA.index, dataA.values, label='Stock A', color='r')
    plt.plot(dataB.index, dataB.values, label='Stock B', color='b')
    plt.title('Stock Price over Time for Stocks A and B')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def simple_kalman_filtered_pair_trading(dataA, dataB, Q=0.1, R=0.1, shares=100, factor=10):
    '''
    Simulates a pair trading strategy aided by a Kalman Filter that
    adjusts the number of shares held in each company based on a filtered
    ratio of the company pair's stock prices
    :param dataA: array of observed stock price data for company A
    :param dataB: array of observed stock price data for company B
    :param shares: float of initial amount of shares held in each company
    :param factor: float of scaling factor for the share amount adjustment
    :return: float of profit percentage
    '''
    ratio = dataA / dataB
    k = kf.KalmanFilter(ratio, Q, R)
    filtered_ratio = k.run()
    sharesA = shares
    sharesB = shares

    process_costs = 0

    # Adjust amount of shares based on observed and filtered ratio difference
    for d in range(1, len(dataA)):
        delta = (filtered_ratio[d] - ratio.iloc[d])
        sharesA += delta * factor
        sharesB += -1 * delta * factor

        # tracking costs of buying/selling stocks
        process_costs += delta * factor * dataA.iloc[d]
        process_costs += -1 * delta * factor * dataB.iloc[d]

    init_holdings = dataA.iloc[0] * shares + dataB.iloc[0] * shares
    fin_holdings = dataA.iloc[-1] * sharesA + dataB.iloc[-1] * sharesB

    return (fin_holdings - process_costs)/ init_holdings

def simple_bollinger_bands_pair_trading(dataA, dataB, shares=100, factor=10):
    '''
   Simulates a pair trading strategy using Bollinger bands that
   adjusts the number of shares held in each company based on the upper
   and lower bollinger band bounds
   :param dataA: array of observed stock price data for company A
   :param dataB: array of observed stock price data for company B
   :param shares: float of initial amount of shares held in each company
   :param factor: float of scaling factor for the share amount adjustment
   :return: float of profit percentage
   '''
    ratio = dataA / dataB
    sma, upper_band, lower_band = bb.bollinger_bands(ratio)
    sharesA = shares
    sharesB = shares

    process_costs = 0

    for i in range(20, len(ratio)):
        if ratio.iloc[i] > upper_band[i]:
            delta = ratio.iloc[i] - upper_band[i]
            sharesA += -1 * delta * factor
            sharesB += delta * factor

            # tracking costs of buying/selling stocks
            process_costs +=  -1 * delta * factor * dataA.iloc[i]
            process_costs += delta * factor * dataB.iloc[i]

        if ratio.iloc[i] < lower_band[i]:
            delta = lower_band[i] - ratio.iloc[i]
            sharesA += delta * factor
            sharesB += -1 * delta * factor

            # tracking costs of buying/selling stocks
            process_costs += delta * factor * dataA.iloc[i]
            process_costs += -1 * delta * factor * dataB.iloc[i]

    init_holdings = dataA.iloc[0] * shares + dataB.iloc[0] * shares
    fin_holdings = dataA.iloc[-1] * sharesA + dataB.iloc[-1] * sharesB

    return (fin_holdings - process_costs)/ init_holdings