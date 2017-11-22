import sys
sys.path.insert(0,'..')
from datetime import datetime as dt
import pandas as pd
from stockstats import StockDataFrame as Sdf
from binance.enums import *
import time

def get_kline_data_from_binance(client,symbol="RDNETH",interval=KLINE_INTERVAL_1HOUR):
    klines = client.get_klines(symbol=symbol, interval=interval)
    d = {"Date":[],"Open":[],"High":[],"Low":[],"Close":[],"Volume":[]}

    for kline in klines:
        [open_time, open_price, high_price, low_price, close_price, volume, close_time,
         quote_asset_volume, number_of_trades,
         taker_buy_base_asset_volume, taker_buy_quote_asset_volume, _] = kline
        timestamp_f = float(open_time/1000.0)
        timestamp = dt.fromtimestamp(timestamp_f)
        d["Date"].append(timestamp)
        d["Open"].append(open_price)
        d["High"].append(high_price)
        d["Low"].append(low_price)
        d["Close"].append(close_price)
        d["Volume"].append(volume)

    df = pd.DataFrame(data=d)
    df['Open'] = df['Open'].astype('float64')
    df['High'] = df['High'].astype('float64')
    df['Low'] = df['Low'].astype('float64')
    df['Close'] = df['Close'].astype('float64')
    df['Volume'] = df['Volume'].astype('float64')
    stat = Sdf.retype(df)
    return (stat,df,d['Date'])
