import boto3
import sys
sys.path.insert(0,'..')
from data.html_helper import check_if_address_name_exists

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table_name = "eth_accounts"
table = dynamodb.Table(table_name)

def put_item(account_address,account_name,rdn_type):
    account_address = account_address.lower()
    table.put_item(
    Item={'account_address': account_address,'account_name':account_name,'rdn_type': rdn_type})

def get_item(account_address):
    response = table.get_item(Key={'account_address': account_address,})
    try:
        item = response['Item']
        if "account_name" in item:
            account_name = item["account_name"]
        else:
            account_name = "N/A"
        if "is_flipping" in item:
            is_flipping = item["is_flipping"]
        else:
            is_flipping = "N/A"
        if "flipping_score" in item:
            flipping_score = str(item["flipping_score"])
        else:
            flipping_score = "N/A"

        return (account_name,is_flipping,flipping_score)
    except:
        return (None,None,None)

def check_for_address_name(address):
    db_name,flip,score = get_item(address)
    if db_name is not None:
        return (db_name,"db")
    else:
        account_name = check_if_address_name_exists(address)
        if account_name != "":
            # flip,score = is_flipping(address)
            flip,score = 1,1
            return (account_name,"scan")
        else:
            return ("","scan")
