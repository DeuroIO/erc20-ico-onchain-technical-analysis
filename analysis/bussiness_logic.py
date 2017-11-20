import sys
sys.path.insert(0,'..')
from data.whale_data import find_whale_account_token_tx
from data.html_helper import check_if_address_name_exists
from db.amazon_db import check_for_address_name,put_item
from data.whale_eth_tx_data import *
from data.whale_token_tx_data import identify_investor_type_token

holding_account = "holding_account"
deposit_account = 'deposit_account'
withdraw_account = "withdraw_account"

def perform_bfs_on_accounts(out_txs,top_holder_type,acc,m_type='OUT'):
    print("\t"+m_type)
    unique_out = set()
    for out in out_txs:
        unique_out.add(out[3])

    for out in unique_out:
        print("\t"+out)
        out_scan_name,source = check_for_address_name(out)
        if out_scan_name != "":
            print("\t\t{}".format(out_scan_name))
            continue
        investor_type = identify_investor_type(out)
        if investor_type == affliate_type:
            investor_type = identify_investor_type_token(out)
        print("\t\t{}".format(investor_type))
        if investor_type == exchange_type:
            top_holder_type[acc] = deposit_account if m_type == "OUT" else withdraw_account
    return top_holder_type

def main_business_logic():
    txs = find_whale_account_token_tx()
    top_holder_type = dict()

    for acc in txs:
        print(acc)
        scan_name = check_if_address_name_exists(acc)
        if scan_name != "":
            print("{}".format(scan_name))
            continue

        a_name,source = check_for_address_name(acc)
        if a_name != "": print("{}".format(a_name))
        tx = txs[acc]

        #如果当前账户从来没有向外打过token,ignore
        out_txs = [item for item in tx if item[2] == 'OUT']
        if len(out_txs) == 0:
            print("\tholding account")
            if scan_name != "": aws_name = scan_name
            elif a_name != "": aws_name = a_name
            else: aws_name = "RDN Top holders"
            put_item(acc,aws_name,"[RDN]holding")
            top_holder_type[acc] = holding_account
            continue

        #在所有OUT账号上做BFS
        top_holder_type = perform_bfs_on_accounts(out_txs,top_holder_type,acc)

        #在所有IN账号上做BFS
        in_txs = [item for item in tx if item[2] == 'IN']
        top_holder_type = perform_bfs_on_accounts(in_txs,top_holder_type,acc,m_type='IN')

    for acc in top_holder_type:
        print("{} {}".format(acc,top_holder_type[acc]))
