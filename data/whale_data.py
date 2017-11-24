from .whale_operation import find_whale_txs
from .html_helper import find_tx_given_token_contract_address

Watch_addr = "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6"    #Radien Network

#Whale operation: etherdelta,binance,liqui.io
exchnage_accounts = ['0x8d12a197cb00d4747a1fe03395095ce2a5cc6819','0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be']


# Escape raiden_multi_sig_wallet
raiden_team_address = "0x00c7122633a4ef0bc72f7d02456ee2b11e97561e"

def find_interstering_accounts():
    # Find accounts
    txs = find_tx_given_token_contract_address(Watch_addr,1,1)
    return txs

def find_whale_account_token_tx():
    all_arr = find_interstering_accounts()
    print("-------------------find_whale_account_token_tx--------------------")
    print("len(all_arr): {}".format(len(all_arr)))
    counter = 0
    acc_features = dict()
    for account in all_arr:
        counter += 1
        print("{}/{} {}".format(counter,len(all_arr),account))
        if account == raiden_team_address or account in exchnage_accounts:
            continue
        else:
            acc_features[account] = find_whale_txs(Watch_addr,account)
    return acc_features

def find_exchange_txs():
    all_arr = exchnage_accounts
    print("-------------------find_exchange_txs--------------------")
    print("len(all_arr): {}".format(len(all_arr)))
    counter = 0
    acc_features = dict()
    for account in all_arr:
        counter += 1
        print("{}/{} {}".format(counter,len(all_arr),account))
        acc_features[account] = find_whale_txs(Watch_addr,account)
    return acc_features
