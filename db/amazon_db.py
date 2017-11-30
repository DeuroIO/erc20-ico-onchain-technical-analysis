import boto3
import sys
sys.path.insert(0,'..')

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

table_name = "eth_accounts"
table = dynamodb.Table(table_name)

def put_item(account_address,account_name,is_flipping=' ',flipping_score=' '):
    account_address = account_address.lower()
    table.put_item(
    Item={'account_address': account_address,'account_name':account_name,'is_flipping': is_flipping,"flipping_score":str(flipping_score)
    })

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
        return db_name
    else:
        return address
