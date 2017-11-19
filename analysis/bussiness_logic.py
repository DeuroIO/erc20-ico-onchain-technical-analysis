import sys
sys.path.insert(0,'..')
from data.whale_data import find_whale_account_token_tx
from data.html_helper import check_if_address_name_exists
from db.amazon_db import check_for_address_name,put_item

def main_business_logic():
    txs = find_whale_account_token_tx()
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
            continue

        print("perform analysis on {}".format(acc))
        #在所有OUT账号上做BFS
        for out in out_txs:
            print("\t{}".format(out))
