import sys
sys.path.insert(0,'..')
from data.whale_data import find_whale_account_token_tx,exchnage_accounts,raiden_team_address
from data.html_helper import check_if_address_name_exists
from db.amazon_db import check_for_address_name,put_item
from data.whale_eth_tx_data import *
from data.whale_token_tx_data import identify_investor_type_token
from plot.plotly_helper import plot_using_plotly

holding_account = "holding_account"
deposit_account = 'deposit_account'
withdraw_account = "withdraw_account"

in_type = "IN"
out_type = "OUT"

all_acc_types = dict()
for acc in exchnage_accounts:
    all_acc_types[acc] = exchange_type

# 保存最早的交易时间
from datetime import datetime
from datetime import timedelta
the_earliest_tx_time = datetime.now()


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

    for out in unique_out:
        print("\t"+out)
        out_scan_name,source = check_for_address_name(out)
        if out_scan_name != "":
            print("\t\t{}".format(out_scan_name))
            continue
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

def main_business_logic():
    txs = find_whale_account_token_tx()
    top_holder_type = dict()

    # 找到最早的交易时间
    global the_earliest_tx_time

    for acc in txs:
        print(acc)

        acc_txs = txs[acc]
        for sub_tx in acc_txs:
            tx_date = sub_tx[0]
            if tx_date < the_earliest_tx_time: the_earliest_tx_time = tx_date

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

    print("------------------------------------------")
    for acc in all_acc_types:
        print("{} {}".format(acc,all_acc_types[acc]))

    # build X time array
    the_earliest_tx_time = the_earliest_tx_time.replace(minute=0, second=0)
    current_time = datetime.now().replace(minute=0, second=0)
    tmp_time = the_earliest_tx_time
    X = []

    while tmp_time < current_time:
        X.append(tmp_time)
        tmp_time += timedelta(hours=1)
    print(len(X))

    # build all traxe Y: holding_amount, deposit_amount, withdraw_amount
    amount_trace_y = [0] * len(X)
    deposit_trace_y = [0] * len(X)
    withdraw_trace_y = [0] * len(X)

    for holder in txs:
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
            elif holder_type == deposit_account:
                if tx_type == out_type and all_acc_types[to_a] == exchange_type:
                    deposit_trace_y = update_y_array(X,deposit_trace_y,timestamp,amount)
            elif holder_type == withdraw_account:
                if tx_type == in_type and all_acc_types[from_a] == exchange_type:
                    withdraw_trace_y = update_y_array(X,withdraw_trace_y,timestamp,amount)
            else:
                print("ERROR!")
                assert(False)

    amount_trace = {"x":X,"y":amount_trace_y,"name":"Holding Amount"}
    deposit_trace = {"x":X,"y":deposit_trace_y,"name":"Exchange Deposit Amount"}
    withdraw_trace = {"x":X,"y":withdraw_trace_y,"name":"Exchange Withdraw Amount"}
    plot_using_plotly("RDN Top Investor Analysis",[amount_trace,deposit_trace,withdraw_trace])
