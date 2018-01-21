from analysis.bussiness_logic import main_business_logic
import data.whale_data as wd
import sys

#exchange_accounts
exchange_accounts = ['0xfbb1b73c4f0bda4f67dca266ce6ef42f520fbb98','0xe94b04a0fed112f3664e45adb2b8915693dd5ff3', #Bittrex
'0x1151314c646ce4e0efd76d1af4760ae66a9fe30f','0xcafb10ee663f465f9d10588ac44ed20ed608c11e','0x7180EB39A6264938FDB3EfFD7341C4727c382153', '0x7727e5113d1d161373623e5f49fd568b4f543a9e','0x4fdd5eb2fb260149a3903859043e962ab89d8ed4',#Bitfinex
'0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be', #Binance
'0xb794f5ea0ba39494ce839613fffba74279579268','0x32be343b94f860124dc4fee278fdcbd38c102d88','0xab11204cfeaccffa63c2d23aef2ea9accdb0a0d5','0x209c4784ab1e8183cf58ca33cb740efbf3fc18ef','0x0536806df512D6cDDE913Cf95c9886f65b1D3462',#poloniex
'0x5E575279bf9f4acf0A130c186861454247394C06','0x8271B2E8CBe29396e9563229030c89679B9470db', #liqui.io]
'0x8d12a197cb00d4747a1fe03395095ce2a5cc6819', #etherdelta
'0xfaabe432a1e6843f3486f11fa360a1e1248677fc', #cex.io
'0x5c985e89dde482efe97ea9f1950ad149eb73829b', #huobi.pro
]
exchange_accounts = [x.lower() for x in exchange_accounts]


def main_func(symbol,Watch_addr,coinmarketcap_symbol):
    wd.Watch_addr = Watch_addr
    wd.exchnage_accounts = exchange_accounts

    escape_accounts = list(exchange_accounts)
    escape_accounts.append("0xead6be34ce315940264519f250d8160f369fa5cd") #ZRX bot
    escape_accounts.append("0x00c7122633a4ef0bc72f7d02456ee2b11e97561e") #Raidne Team
    escape_accounts.append("0x615ed6779507f223d04722d43ccc0cd871964e2a") #GTO Team
    escape_accounts.append("0xe16fd9b95758fe8f3a478ef9b750a64513bf2e80") # ICX team)
    escape_accounts.append("0x6863424c64081d69a9f23f780bb3c73dddbf15f6") # THETA team)
    escape_accounts.append("0x30993352B0e5a02A5ea2A7711FD7C97a4401D654") # Theta team
    escape_accounts.append("0x03E130eaFAB61ca4D31923B4043db497a830D2bD") # Theta team
    escape_accounts.append("0xb65Ad53b13B3c7a89527164Fe69CcD56FcEba1B9") # theta team
    
    return main_business_logic(symbol,escape_accounts,coinmarketcap_symbol)

def driver_to_run_main_func(data):
    plot_dict = dict()

    for symbol in data:
        coin_symbol,Watch_addr = data[symbol]
        print("{} {} {}".format(symbol,coin_symbol,Watch_addr))
        plots = main_func(symbol,Watch_addr,coin_symbol)
        plot_dict[symbol] = plots

    for symbol in plot_dict:
        coin_symbol,Watch_addr = data[symbol]
        print("{} {} {}".format(symbol,coin_symbol,Watch_addr))
        plots = plot_dict[symbol]
        for plot in plots:
            print("\t{} {}\n".format(plot,plots[plot]))
import time
if __name__ == "__main__":
    data = {
        # "OMG": ('omisego','0xd26114cd6EE289AccF82350c8d8487fedB8A0C07'),
        # 'SNT': ('status','0x744d70fdbe2ba4cf95131626614a1763df805b9e'),
        # 'CVC': ('civic','0x41e5560054824ea6b0732e656e3ad64e20e94e45'),
        # 'MTL': ('metal','0xF433089366899D83a9f26A773D59ec7eCF30355e'),
        # 'ADX': ('adx-net','0x4470BB87d77b963A013DB939BE332f927f2b992e'),
        # 'KNC': ('kyber-network','0xdd974d5c2e2928dea5f71b9825b8b646686bd200'),
        # 'ZRX': ('0x','0xe41d2489571d322189246dafa5ebde1f4699f498'),
        # 'RDN': ('raiden-network-token','0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6')
        #'GTO' : ('gifto','0xc5bbae50781be1669306b9e001eff57a2957b09d')
        'THETA' : ('theta-token','0x3883f5e181fccaF8410FA61e12b59BAd963fb645')
    }
    driver_to_run_main_func(data)
