import pandas as pd
import time
import requests
def rti(your_btc_address):
    transactions_url = 'https://blockchain.info/rawaddr/' + your_btc_address
    data = requests.get(transactions_url)
    print(data.headers['Retry-After'])

    df = pd.read_json(transactions_url)
    transactions = df['txs']
    time.sleep(5)
    return transactions.values

rtis = pd.DataFrame()
df = pd.read_csv('InputAddress.csv')
rtim = []
xx = df['address'].values
rtil = []
for your_btc_address in xx[:10]:
    rtil.append(rti(your_btc_address))

df1 = pd.DataFrame()
df1['timestamp'] = rtil
df1.to_csv('rti.csv')





