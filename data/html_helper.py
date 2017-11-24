import datetime
from bs4 import BeautifulSoup
import cfscrape


def parse_date(target_data):
    target_data = target_data.replace(minute=0, hour=0, second=0, microsecond=0)
    return target_data

def get_today():
    return parse_date(datetime.datetime.utcnow())

url_content_cache = dict()

def get_html_by_url(url):
    if url not in url_content_cache:
        scraper = cfscrape.create_scraper()
        html = scraper.get(url).content
        soup = BeautifulSoup(html,"lxml")
        url_content_cache[url] = soup
    else:
        soup = url_content_cache[url]
    return soup

def find_token_tx_helper(url):
    soup = get_html_by_url(url)
    if soup is None:
        return []
    trs = soup.findAll("tr")
    tx_arr = []
    for tr_index,tr in enumerate(trs):
        if tr_index != 0:
            # print("tr_index:{}".format(tr_index))
            tds = tr.findAll("td")
            for td_index,td in enumerate(tds):
                if td_index == 1:
                    # from_Address
                    m_a = td.find("a")
                    if m_a is None:
                        m_a = td.find("span")
                    from_address = m_a.text
                    # print("from_address:{}".format(from_address))
            from_address = from_address.lower()
            tx_arr.append(from_address)
    return tx_arr

def get_total_number_of_page(url):
    soup = get_html_by_url(url)
    try:
        d_s = soup.findAll("b")
        return int(d_s[1].text)
    except:
        return 1

def find_tx_given_token_contract_address(contract_address,start_page,end_page):
    url = "https://etherscan.io/token/generic-tokenholders2?a={}".format(contract_address)
    total_number_of_page = get_total_number_of_page(url)
    tx_arrs = []
    print("total_number_of_page:{} for {}".format(total_number_of_page,contract_address))
    for i in range(start_page,end_page+1):
        print(i)
        tx_arr = find_token_tx_helper("{}&p={}".format(url,i))
        tx_arrs = tx_arrs + tx_arr
    return tx_arrs

def check_if_address_name_exists(account):
    url = "https://etherscan.io/address/{}".format(account)
    soup = get_html_by_url(url)
    name = soup.find("font",{"title":"NameTag"})
    if name is not None:
        return name.text
    else:
        return ""
