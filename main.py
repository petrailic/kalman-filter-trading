# Trying Kalman Filter for Pair Trading on Real Data

import kalmanFilter as kf
import pairTrading as pt
import yfinance as yf

def main():
    # Stock price data for two related assets: Coca-Cola and Pepsi
    tickers = yf.Tickers("ko pep")
    dataA = tickers.tickers['KO'].history(start="2024-01-01", end="2024-09-30")['Close']
    dataB = tickers.tickers['PEP'].history(start="2024-01-01", end="2024-09-30")['Close']

    # check correlation
    pt.plot_pair_prices(dataA, dataB)

    # visualize kalman filter application
    kf.plot_kalman_filter_on_stock_ratio(dataA, dataB)

    # run simple pair trading strategy
    p = pt.simple_kalman_filtered_pair_trading(dataA, dataB)                    # TODO: optimize params?
    print('Profit %:', p)

if __name__ == '__main__':
    main()

