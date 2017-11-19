from data.whale_data import find_whale_account_token_tx
from data.html_helper import check_if_address_name_exists

bfs_max_depth = 2

txs = find_whale_account_token_tx()
for acc in txs:
    a_name = check_if_address_name_exists(acc)
    if a_name != "":
        print("{} {}".format(a_name,acc))
    else:
        print(acc)
