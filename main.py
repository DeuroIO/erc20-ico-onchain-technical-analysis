from analysis.bussiness_logic import main_business_logic
from binance.client import Client
import sys

encry_pass = sys.argv[1]
client = Client(encry_pass, "txts/binance")
main_business_logic(client)
