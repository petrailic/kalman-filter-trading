# Trying Kalman Filter for Pair Trading on Real Data

import kalmanFilter as kf
import pairTrading as pt
import yfinance as yf
import bollingerBands as bb


def kalman():
    # Stock price data for two related assets: Coca-Cola and Pepsi
    tickers = yf.Tickers("ko pep")
    dataA = tickers.tickers['KO'].history(start="2024-01-01", end="2024-09-30")['Close']
    dataB = tickers.tickers['PEP'].history(start="2024-01-01", end="2024-09-30")['Close']

    # check correlation
    pt.plot_pair_prices(dataA, dataB)
    #plt.savefig('pair_plot')

    # visualize kalman filter application
    kf.plot_kalman_filter_on_stock_ratio(dataA, dataB)
    #plt.savefig('kalman_plot')

    # run simple pair trading strategy
    p = pt.simple_kalman_filtered_pair_trading(dataA, dataB)
    print('Kalman Profit %:', p)

def bollinger():
    tickers = yf.Tickers("ko pep")
    # 20 day pre-period for historical data needed for bollinger bands (real start 2024-01-01)
    dataA = tickers.tickers['KO'].history(start="2023-12-12", end="2024-09-30")['Close']
    dataB = tickers.tickers['PEP'].history(start="2023-12-12", end="2024-09-30")['Close']

    ratio = dataA / dataB

    # visualize bollinger bands
    bb.plot_bollinger_bands(ratio)

    # run simple pair trading strategy
    p = pt.simple_bollinger_bands_pair_trading(dataA, dataB)
    print('Bollinger Profit %:', p)

def main():
    kalman()
    bollinger()

if __name__ == '__main__':
    main()

