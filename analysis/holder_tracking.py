# calculate holder number over time
# input: acc_holding_values_dict
#           key:    timestamp
#           value:  dict
#                   key:    account
#                   value:  amount
MINIMUM_TOKEN_AMOUNT_REQUIRED = 0.0

def track_holder_number_over_time(acc_holding_values_dict):
    holder_number_over_time = []
    for timestamp in acc_holding_values_dict:
        number = 1
        t_dict = acc_holding_values_dict[timestamp]
        print(timestamp)
        for acc in t_dict:
            if t_dict[acc] > MINIMUM_TOKEN_AMOUNT_REQUIRED:
                number += 1
                print("\t{}:{}".format(acc,t_dict[acc]))
        holder_number_over_time.append(number)
    return holder_number_over_time
