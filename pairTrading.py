# Simple Pair Trading Strategy with Kalman Filter

import kalmanFilter as kf
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
    f = factor

    # Adjust amount of shares based on observed and filtered ratio difference
    for d in range(1, len(dataA)):
        delta = (filtered_ratio[d] - ratio.iloc[d])
        sharesA += delta * f
        sharesB += -1 * delta * f

    init_holdings = dataA.iloc[0] * shares + dataB.iloc[0] * shares
    fin_holdings = dataA.iloc[-1] * sharesA + dataB.iloc[-1] * sharesB
    return fin_holdings/ init_holdings