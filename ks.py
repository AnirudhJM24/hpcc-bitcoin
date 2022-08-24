import pandas as pd
import time

# rtis = pd.DataFrame()
# df = pd.read_csv('InputAddress.csv')
# rtim = []
# xx = df['address'].values
# for your_btc_address in xx[:10]:
def rti(your_btc_address):
    transactions_url = 'https://blockchain.info/rawaddr/' + your_btc_address

    df = pd.read_json(transactions_url)
    transactions = df['txs']

    rti = list()
    for i in range(1,len(transactions)-1):
        rti.append(-1*(transactions[i+1]['time']-transactions[i]['time']))
    return rti

#address1 = "3DizHPsBkvQnT7KcDeovG9Q7TxqczViC4m"
#address2 = "32QQnF2H3DAfPBxaPwTpD7KL6x6U4g1Jtq"
address1 = "1taKuQAcYTP8VUbxsGu4Byi38xsay952v"
address2 = "bc1qwuwqj4k6fn7t6zytyenz55wwt26k9dnv9y6k5n"
rti1 = rti(address1)
rti2 = rti(address2)
from scipy import stats
result = stats.ks_2samp(rti1, rti2)
print(result)
import matplotlib.pyplot as plt
rtix1 = [i for i in range(0,len(rti1))]
rtix2 = [i for i in range(0,len(rti2))]
plt.plot(rti1,'b',rti2,'r')
plt.title('KS TEST')
plt.legend(['address:'+ address1,'address:'+ address2], loc = 'upper right')
plt.xlabel('index')
plt.ylabel('RTI')
plt.savefig('timeseries.jpg')
plt.show()
#plt.savefig('timeseries.jpg')

