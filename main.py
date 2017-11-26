from analysis.bussiness_logic import main_business_logic
import data.whale_data as wd
import sys

symbol = 'KNC'
coinmarketcap_symbol = 'kyber-network'
Watch_addr = "0xdd974d5c2e2928dea5f71b9825b8b646686bd200"

symbol = 'ZRX'
coinmarketcap_symbol = '0x'
Watch_addr = "0xe41d2489571d322189246dafa5ebde1f4699f498"

symbol = 'RDN'
coinmarketcap_symbol = 'raiden-network-token'
Watch_addr = "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6"

symbol = 'OMG'
coinmarketcap_symbol = 'omisego'
Watch_addr = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"    #OmeisGo

symbol = 'SNT'
coinmarketcap_symbol = 'status'
Watch_addr = "0x744d70fdbe2ba4cf95131626614a1763df805b9e"

symbol = 'CVC'
coinmarketcap_symbol = 'civic'
Watch_addr = "0x41e5560054824ea6b0732e656e3ad64e20e94e45"

symbol = 'MTL'
coinmarketcap_symbol = 'metal'
Watch_addr = "0xF433089366899D83a9f26A773D59ec7eCF30355e"

symbol = 'ADX'
coinmarketcap_symbol = 'adx-net'
Watch_addr = '0x4470BB87d77b963A013DB939BE332f927f2b992e'

#exchange_accounts Poloniex
exchange_accounts = ['0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98','0xe94b04a0fed112f3664e45adb2b8915693dd5ff3', #Bittrex
'0x1151314c646ce4e0efd76d1af4760ae66a9fe30f','0xcafb10ee663f465f9d10588ac44ed20ed608c11e','0x7180EB39A6264938FDB3EfFD7341C4727c382153', '0x7727e5113d1d161373623e5f49fd568b4f543a9e','0x4fdd5eb2fb260149a3903859043e962ab89d8ed4',#Bitfinex
'0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be', #Binance
'0xb794f5ea0ba39494ce839613fffba74279579268','0x32be343b94f860124dc4fee278fdcbd38c102d88','0xab11204cfeaccffa63c2d23aef2ea9accdb0a0d5','0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef','0x0536806df512D6cDDE913Cf95c9886f65b1D3462',#poloniex
'0x5E575279bf9f4acf0A130c186861454247394C06','0x8271B2E8CBe29396e9563229030c89679B9470db', #liqui.io]
'0x8d12a197cb00d4747a1fe03395095ce2a5cc6819' #etherdelta
]
exchange_accounts = [x.lower() for x in exchange_accounts]

wd.Watch_addr = Watch_addr
wd.exchnage_accounts = exchange_accounts

escape_accounts = list(exchange_accounts)
escape_accounts.append("0xead6be34ce315940264519f250d8160f369fa5cd") #ZRX bot

main_business_logic(symbol,escape_accounts,coinmarketcap_symbol)
