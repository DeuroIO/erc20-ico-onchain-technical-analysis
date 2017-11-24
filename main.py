from analysis.bussiness_logic import main_business_logic
from binance.client import Client
import data.whale_data as wd
import sys

symbol = 'OMG'
Watch_addr = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"    #OmeisGo
# Bittrex, Bitfinex, Binance, Poloniex
exchange_accounts = ['0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98','0x1151314c646ce4e0efd76d1af4760ae66a9fe30f','0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be']
# OMG bot accounts. escape
escape_accounts = ['0x36b01066b7fa4a0fdb2968ea0256c848e9135674']

wd.Watch_addr = Watch_addr
wd.exchnage_accounts = exchange_accounts

encry_pass = sys.argv[1]
client = Client(encry_pass, "txts/binance")
main_business_logic(client,symbol,escape_accounts)
