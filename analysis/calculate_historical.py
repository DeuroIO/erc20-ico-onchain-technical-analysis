import operator
import sys
sys.path.insert(0,'..')
from db.amazon_db import check_for_address_name

in_type = "IN"
out_type = "OUT"

def calculate_historical_holders(txs,X):

    # init acc_holding_values_dict
    acc_holding_values_dict = dict()
    dummy_acc_dict = dict()
    for acc in txs:
        dummy_acc_dict[acc] = 0
    for t in X:
        acc_holding_values_dict[t] = dummy_acc_dict.copy()

    # populate acc_holding_values_dict
    for acc in txs:
        a_txs = txs[acc]
        for m_tx in a_txs:
            [t,from_a,tx_type,to_a,quantity] = m_tx
            for x_t in X:
                if x_t >= t:
                    t_dict = acc_holding_values_dict[x_t]
                    if tx_type == in_type:
                        t_dict[to_a] += quantity
                    else:
                        t_dict[from_a] -= quantity

                    acc_holding_values_dict[x_t] = t_dict

    return acc_holding_values_dict

def find_top_50_over_time_helper(acc_holding_values_dict):
    top_50_holding_values = dict()
    for t in acc_holding_values_dict:
        acc_list_at_time_t = acc_holding_values_dict[t]
        sorted_x = sorted(acc_list_at_time_t.items(), key=operator.itemgetter(1),reverse=True)[:50]

        sorted_dict = dict()
        for key, value in sorted_x:
            sorted_dict[key] = float(value)
        top_50_holding_values[t] = sorted_dict

    return top_50_holding_values

def calculate_top_50_token_moving_average(top_50_holding_values):
    top_50_token_moving_average_trace = []
    for t in top_50_holding_values:
        curr_sum = 0.0
        accs = top_50_holding_values[t]
        for acc in accs: curr_sum += accs[acc]
        curr_sum /= 50
        top_50_token_moving_average_trace.append(curr_sum)
    return top_50_token_moving_average_trace

def calculate_top_50_list_and_token_amount_change(top_50_holding_values):
    top_50_list_and_token_amount_change_trace = []
    unique_acc_set = set()
    acc_name_dict = dict()

    for t in top_50_holding_values:
        accs = top_50_holding_values[t]
        for acc in accs:
            if acc not in unique_acc_set:
                unique_acc_set.add(acc)
                acc_name = check_for_address_name(acc)
                acc_name_dict[acc] = acc_name
                top_50_list_and_token_amount_change_trace.append({"name":acc_name,'x':[t],'y':[accs[acc]]})
            else:
                for json in top_50_list_and_token_amount_change_trace:
                    acc_name = acc_name_dict[acc]
                    if json['name'] == acc_name:
                        json['x'].append(t)
                        json['y'].append(accs[acc])

    return top_50_list_and_token_amount_change_trace
# def calculate_top_50_holding_token_amount(acc_holding_values_dict):
