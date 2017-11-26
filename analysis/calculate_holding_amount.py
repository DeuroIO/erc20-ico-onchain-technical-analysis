import sys
sys.path.insert(0,'..')
from data.whale_data import find_whale_account_token_tx,exchnage_accounts
from data.html_helper import check_if_address_name_exists
from data.whale_eth_tx_data import *
from data.whale_token_tx_data import identify_investor_type_token

holding_account = "holding_account"
deposit_account = 'deposit_account'
withdraw_account = "withdraw_account"

in_type = "IN"
out_type = "OUT"

all_acc_types = dict()
for acc in exchnage_accounts:
    all_acc_types[acc] = exchange_type


def update_y_array(X,y,timestamp,amount):
    target_index = 0
    for i in range(len(X)):
        x_time = X[i]
        if timestamp < x_time:
            target_index = i
            break

    for i in range(target_index,len(y)):
        y[i] += amount

    return y

def perform_bfs_on_accounts(out_txs,top_holder_type,acc,m_type='OUT'):
    print("\t"+m_type)
    unique_out = set()
    for out in out_txs:
        unique_out.add(out[3])
    unique_out = list(unique_out)[:5]
    for out in unique_out:
        print("\t"+out)
        if out not in all_acc_types:
            investor_type = identify_investor_type(out)
            if investor_type == affliate_type:
                investor_type = identify_investor_type_token(out)
            print("\t\t{}".format(investor_type))
        else:
            investor_type = all_acc_types[out]
        if investor_type == exchange_type:
            top_holder_type[acc] = deposit_account if m_type == "OUT" else withdraw_account
        all_acc_types[out] = investor_type

    if acc not in top_holder_type:
        top_holder_type[acc] = holding_account

    return top_holder_type

def calculate_holding_amount(X,escape_accounts):
    txs = find_whale_account_token_tx(escape_accounts)
    top_holder_type = dict()

    for acc in txs:
        print(acc)
        tx = txs[acc]

        #如果当前账户从来没有向外打过token,ignore
        out_txs = [item for item in tx if item[2] == 'OUT']
        if len(out_txs) == 0:
            print("\tholding account")
            top_holder_type[acc] = holding_account
            continue

        if acc in escape_accounts:
            continue

        #在所有OUT账号上做BFS
        top_holder_type = perform_bfs_on_accounts(out_txs,top_holder_type,acc)

        #在所有IN账号上做BFS
        in_txs = [item for item in tx if item[2] == 'IN']
        top_holder_type = perform_bfs_on_accounts(in_txs,top_holder_type,acc,m_type='IN')

    # build all traxe Y: holding_amount, deposit_amount, withdraw_amount
    amount_trace_y = [0] * len(X)

    for holder in txs:
        if holder in escape_accounts:
            continue
        if holder not in top_holder_type:
            print("{} not identified! ".format(holder))
            continue

        holder_type = top_holder_type[holder]
        holder_txs = txs[holder]
        print("{} {}".format(holder,holder_type))

        for tx in holder_txs:
            [timestamp,from_a,tx_type,to_a,amount] = tx
            if holder_type == holding_account:
                if tx_type == in_type:
                    amount_trace_y = update_y_array(X,amount_trace_y,timestamp,amount)
                else:
                    amount_trace_y = update_y_array(X,amount_trace_y,timestamp,-amount)

    return amount_trace_y
