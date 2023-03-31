from requests import get
from datetime import datetime
from matplotlib import pyplot as plt
import json
import config

BASE_URL = "https://api.etherscan.io/api"
ETHER_TO_GWEI = 10**18
address = "0x130093A5aEbc07e78e16f0EcEF09d1c45AfD8178"
file_name = 'lexdao_transaction_history.json'


def make_api_url(module, action, address, **kwargs):
        url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={config.api_key}"

        for key, value in kwargs.items():
            url += f"&{key}={value}"
        
        return url


def get_transactions(address):
      get_transactions_url = make_api_url("account", "txlist", address, startblock=0, endblock=99999999, page=1, offset=10000, sort="asc")
      response = get(get_transactions_url)
      data = response.json()["result"]
      for tx in data:
         blocknumber = tx["blockNumber"]
         hash = tx["hash"]
         to = tx["to"]
         from_addr = tx["from"]
         eth_quantity= int(tx["value"]) / ETHER_TO_GWEI
         eth_gas = int(tx["gasUsed"]) * int(tx["gasPrice"]) / ETHER_TO_GWEI #I'm not clear why this needs to be multiplied for gas but not Ethereum Value
         eth_total = eth_gas + eth_quantity
         time = datetime.fromtimestamp(int(tx["timeStamp"]))
         
      print(len(data))
      with open(file_name, 'w') as f:
            json.dump(data, f, indent = 4)


get_transactions(address)

