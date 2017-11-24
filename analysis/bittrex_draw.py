import requests
import pandas as pd
from dateutil.parser import parse

def bittrex_kline_data(symbol):
    url = 'https://bittrex.com/Api/v2.0/pub/market/GetTicks?marketName={}&tickInterval=hour'.format(symbol)
    data = requests.get(url).json()['result']
    d = {"date":[],"open":[],"high":[],"low":[],"close":[],"volume":[]}
    for kline in data:
        [open_time, high_price,low_price,open_price, close_price, volume] = kline['T'],kline['H'],kline['L'],kline['O'],kline['C'],kline['V']
        timestamp = parse(open_time)
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
    df,df_2,d = bittrex_kline_data('BTC-ADX')
    print(df)
