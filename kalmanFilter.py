import numpy as np
import matplotlib.pyplot as plt

class KalmanFilter:
    '''
    :param data: array of observed data
    :param Q: float of process noise
    :param R: float of measurement noise
    :return: array of filtered data
    '''
    def __init__(self, data, Q=0.1, R=0.1):
        self.data = data
        self.size = len(data)
        self.Q = Q
        self.R = R

        # Initializing state variable and covariance
        self.x =  np.zeros(self.size)                     # State variable
        self.x_prev = np.zeros(self.size)
        self.P = np.zeros(self.size)                      # State covariance
        self.P_prev = np.zeros(self.size)

        # Setting first state to be the first observed data value for quicker fitting
        self.x[0] = data.iloc[0]

    def predict(self, i):
        self.x_prev[i] = self.x[i - 1]
        self.P_prev[i] = self.P[i - 1] + self.Q

    def update(self, i):
        K = self.P_prev[i] / (self.P_prev[i] + self.R)  # Kalman Gain
        self.x[i] = self.x_prev[i] + K * (self.data.iloc[i] - self.x_prev[i])
        self.P[i] = (1 - K) * self.P_prev[i]

    def run(self):
        for i in range(1, self.size):
            self.predict(i)
            self.update(i)
        return self.x

def plot_kalman_filter_on_stock_ratio(dataA, dataB, Q=0.1, R=0.1):
    ratio = dataA / dataB
    k = KalmanFilter(ratio, Q ,R)
    filtered_ratio = k.run()

    # Plotting observed and filtered ratios
    plt.plot(ratio.index, ratio.values, label='Observed Ratio', color='k')
    plt.plot(ratio.index, filtered_ratio, label='Filtered Ratio', color='r')

    plt.title('Kalman Filter on Stock Ratio for Pair Trading')
    plt.xlabel('Date')
    plt.ylabel('Price Ratio')
    plt.legend()
    plt.show()
