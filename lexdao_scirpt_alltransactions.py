from requests import get
from matplotlib import pyplot as plt
from datetime import datetime
import config


BASE_URL = "https://api.etherscan.io/api"
ETHER_TO_GWEI = 10**18
address = "0x5a741ab878bb65f6ae5506455fb555eaf3094b3f"

def make_api_url(module, action, address, **kwargs):
        url = BASE_URL + f"?module={module}&action={action}&address={address}&apikey={config.api_key}"

        for key, value in kwargs.items():
            url += f"&{key}={value}"
        
        return url


def get_account_balance(address):
   get_balance_url = make_api_url("account", "balance", address, tags="latest", x="2")
   response = get(get_balance_url)
   data = response.json()
   value = print(int(data["result"]) / ETHER_TO_GWEI)
   return value

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
   
         
         print("--------------------")
         print("Time:", time)
         print("Hash:", hash)
         print("From:", from_addr)
         print("To:", to)
         print("Token Quantity:", eth_quantity)
         print("Gas Cost:",eth_gas)
         print("Transaction Total:", eth_total)
         print("Block Number:", blocknumber)


address = "0x5a741ab878bb65f6ae5506455fb555eaf3094b3f"
get_transactions(address)



'''https://api.etherscan.io/api
   ?module=account
   &action=txlist
   &address=0xc5102fE9359FD9a28f877a67E36B0F050d81a3CC
   &startblock=0
   &endblock=99999999
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken'''

'''https://api.etherscan.io/api
   ?module=account
   &action=txlistinternal
   &address=0x2c1ba59d6f58433fb1eaee7d20b26ed83bda51a3
   &startblock=0
   &endblock=2702578
   &page=1
   &offset=10
   &sort=asc
   &apikey=YourApiKeyToken '''

'''https://api.etherscan.io/api
   ?module=account
   &action=balance
   &address=0x5a741ab878bb65f6ae5506455fb555eaf3094b3f
   &tag=latest
   &apikey=YourApiKeyToken'''