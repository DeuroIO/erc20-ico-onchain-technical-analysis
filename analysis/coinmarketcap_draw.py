import requests
import pandas as pd
from dateutil.parser import parse
import numpy as np

def coinmarketcap_data(symbol):
    url = 'https://graphs.coinmarketcap.com/currencies/{}/'.format(symbol)
    data = requests.get(url).json()

    market_cap_by_available_supply = data['market_cap_by_available_supply']
    df = pd.DataFrame(np.array(market_cap_by_available_supply), columns = ['time','market_cap'])
    df['time'] = pd.to_datetime(df['time'], unit='ms')
    df['market_cap'] = df['market_cap'].astype('float64')
    df.set_index('time', inplace=True)

    price_btc = data['price_btc']
    price_btc = [i[1] for i in price_btc]
    se = pd.Series(price_btc)
    df['price_btc'] = se.values
    df['price_btc'] = df['price_btc'].astype('float64')

    price_usd = data['price_usd']
    price_usd = [i[1] for i in price_usd]
    se = pd.Series(price_usd)
    df['price_usd'] = se.values
    df['price_usd'] = df['price_usd'].astype('float64')

    volume_usd = data['volume_usd']
    volume_usd = [i[1] for i in volume_usd]
    se = pd.Series(volume_usd)
    df['volume_usd'] = se.values
    df['volume_usd'] = df['volume_usd'].astype('float64')

    return (df,df.index.values)

if __name__ == "__main__":
    df,times = coinmarketcap_data('0x')
    print(df)
    print(times)
