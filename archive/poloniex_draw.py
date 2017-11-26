import requests
import pandas as pd
from datetime import datetime as dt

def poloniex_kline_data(symbol,start_time=0,end_time=9999999999):
    url = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period=1800'.format(symbol,start_time,end_time)
    data = requests.get(url).json()
    d = {"date":[],"open":[],"high":[],"low":[],"close":[],"volume":[]}
    for kline in data:
        [open_time, high_price,low_price,open_price, close_price, volume] = kline['date'],kline['high'],kline['low'],kline['open'],kline['close'],kline['volume']
        timestamp = dt.fromtimestamp(int(open_time))
        d["date"].append(timestamp)
        d["open"].append(open_price)
        d["high"].append(high_price)
        d["low"].append(low_price)
        d["close"].append(close_price)
        d["volume"].append(volume)

    df = pd.DataFrame(data=d)
    df['open'] = df['open'].astype('float64')
    df['high'] = df['high'].astype('float64')
    df['low'] = df['low'].astype('float64')
    df['close'] = df['close'].astype('float64')
    df['volume'] = df['volume'].astype('float64')
    return (df,df,d['date'])

if __name__ == "__main__":
    df,df_2,d = poloniex_kline_data('ETH_CVC',0)
    print(df)
