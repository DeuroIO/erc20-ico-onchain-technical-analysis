from flipping_address_name import check_number_of_page
from html_helper import get_html_by_url
import pandas as pd
from collections import OrderedDict
from amazon_db import check_for_address_name
import sys
from tabulate import tabulate
import humanfriendly

def extract_token_tx(soup):
    trs = soup.find("div",{"class":"table-responsive"}).findAll("tr")
    tx_arr = []
    for tr_index,tr in enumerate(trs):
        if tr_index != 0:
            # print("tr_index:{}".format(tr_index))
            tds = tr.findAll("td")
            for td_index,td in enumerate(tds):
                if td_index == 1:
                    timestamp = td.find("span")["title"]
                elif td_index == 2:
                    #from
                    from_address = td.find("span").text.lower()
                    span = td.find("span")
                    if span.findChildren('a'):
                        from_address = span.find("a")["href"][9:-10]

                elif td_index == 3:
                    # type
                    tx_type = td.find("span").text
                    if "IN" in tx_type:
                        tx_type = "IN"
                elif td_index == 4:
                    #to
                    to_address = td.find("span").text.lower()
                    span = td.find("span")
                    if span.findChildren('a'):
                        to_address = span.find("a")["href"][9:-10]
                elif td_index == 5:
                    quantity = float(td.text.replace(",",""))
                elif td_index == 6:
                    token_name = td.find("a").text.replace(" ","")
            tx_arr.append([timestamp,from_address,tx_type,to_address,quantity,token_name])
    return tx_arr

def get_all_token_txs(account):
    url = "https://etherscan.io/tokentxns?a={}".format(account)
    soup = get_html_by_url(url)

    no_matching_exist = soup.find("font",{"color":"black"})
    if no_matching_exist is not None:
        return None

    # Get all the token txs
    txs = extract_token_tx(soup)
    total_number_of_page = check_number_of_page(soup)

    if total_number_of_page != 1:
        for x in range(2,total_number_of_page+1):
            tmp_url = url+"&p="+str(x)
            soup = get_html_by_url(tmp_url)
            tmp_txs = extract_token_tx(soup)
            txs += tmp_txs

    return df

def main_token_tx(account):
    df = get_all_token_txs(account)
    parse_token_tx(df,account)
    return df

if __name__ == "__main__":
    main_token_tx(sys.argv[1])
