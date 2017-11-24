import requests
import pandas as pd
from datetime import datetime as dt

def poloniex_kline_data(symbol,start_time=0,end_time=9999999999):
    url = 'https://poloniex.com/public?command=returnChartData&currencyPair={}&start={}&end={}&period=1800'.format(symbol,start_time,end_time)
    data = requests.get(url).json()
    d = {"Date":[],"Open":[],"High":[],"Low":[],"Close":[],"Volume":[]}
    for kline in data:
        [open_time, high_price,low_price,open_price, close_price, volume] = kline['date'],kline['high'],kline['low'],kline['open'],kline['close'],kline['volume']
        timestamp = dt.fromtimestamp(int(open_time))
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
    return (df,df,d['Date'])

if __name__ == "__main__":
    df,df_2,d = poloniex_kline_data('ETH_CVC',0)
    print(df)
