#ignoring warnings
# import warnings
# warnings.simplefilter('ignore')
#
# #importing neccesary modules
# import sys
# import pandas as pd
# import numpy as np
# import matplotlib
# import matplotlib.pyplot as plt
# plt.style.use('seaborn-whitegrid')
# import seaborn as sns
#
# import sklearn
# from sklearn.linear_model import LinearRegression, SGDRegressor
# from sklearn.svm import SVR
# from sklearn.ensemble import BaggingRegressor, RandomForestRegressor
# from sklearn.preprocessing import StandardScaler, MinMaxScaler
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from sklearn.externals import joblib
# from sklearn.model_selection import GridSearchCV, train_test_split
#
# import xgboost
# from xgboost import XGBRegressor, DMatrix

import fxcmpy
import pandas as pd
import datetime as dt
# from pylab import plt
from _thread import start_new_thread


# globalPeriod = 'm1'
# con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')

# if con.is_connected():
#     sys.exit(1)


# get data

# def get_historical_data(start='', end='', instrument='EUR/USD', period='m1', number=250):
#     if start == '':
#         start = dt.datetime(2017, 1, 1)
#     if end == '':
#         end = dt.datetime(2019, 7, 22)
#     return con.get_candles(instrument, period=period, start=start, stop=end, number=number)


# def get_all_instruments():
#     return con.get_instruments()


# def sell(instrument='EUR/USD', pip=100):
#     return con.create_market_sell_order(instrument, pip)


# def buy(instrument='EUR/USD', pip=100):
#     return con.create_market_buy_order(instrument, pip)


# def get_positions():
#     return con.get_open_positions().T


# def on_tick():
#     return 1


def get_csv():
    df = pd.read_csv('data/eurusd_minute.csv').head(100)
    return df

# start_new_thread(heron,)

# print(GetHistoricalData)

from dema import dema

if __name__ == '__main__':
    bid_close = get_csv()
    dema = dema(bid_close['BidClose'])

    for i in range(len(bid_close)):
        print(bid_close[i], dema[i])


