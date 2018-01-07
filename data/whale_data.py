from .whale_operation import find_whale_txs
from .html_helper import find_tx_given_token_contract_address
import datetime
import time

Watch_addr = "0x255aa6df07540cb5d3d297f0d0d4d84cb52bc8e6"    #Radien Network

#Whale operation: etherdelta,binance,liqui.io
exchnage_accounts = ['0x8d12a197cb00d4747a1fe03395095ce2a5cc6819','0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be']

def find_interstering_accounts(start=1,end=1):
    # Find accounts
    txs,total_number_of_pages = find_tx_given_token_contract_address(Watch_addr,start,end)
    return txs,total_number_of_pages

def find_whale_account_token_tx(escape_accounts,start,end):
    all_arr,_ = find_tx_given_token_contract_address(Watch_addr,start,end)
    print("-------------------find_whale_account_token_tx--------------------")
    print("len(all_arr): {}".format(len(all_arr)))
    counter = 0
    acc_features = dict()
    for account in all_arr:
        counter += 1
        if account in escape_accounts:
            continue
        else:
            print("{}/{} {}".format(counter,len(all_arr),account))
            num_txs = find_whale_txs(Watch_addr,account)
            while len(num_txs) == 0:
                time.sleep(1)
                print("\tnumber of txs:{}".format(num_txs))
                num_txs = find_whale_txs(Watch_addr,account)
            acc_features[account] = num_txs
        time.sleep(1)
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
        time.sleep(1)
    return acc_features
