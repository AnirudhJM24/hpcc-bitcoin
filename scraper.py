import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import sys
import os
os.chmod('/home/anirudh/Documents/hpcc/chromedriverf', 0o755)
def main():
    exe_path = 'chromedriverf/chromedriver'
    driver = webdriver.Chrome(exe_path)
    driver.implicitly_wait(0)
    inp_ad_csv = pd.read_csv('InputAddress.csv')
    inp_ad = inp_ad_csv['address'].values
    search50 = []
    for i in inp_ad[15:25]:
        print(i)
        dfi = pd.DataFrame()
        hash = []
        timestamp = []
        value = []
        outputadd = []
        ts_url = 'https://www.blockchain.com/btc/address/' + i
        driver.get(ts_url)

        search = driver.find_elements(By.XPATH, './/div[@class="sc-1fp9csv-0 ifDzmR"]')
        for ts in search:
            
                txhash = ts.find_element(By.XPATH,'.//a[@class="sc-1r996ns-0 fLwyDF sc-1tbyx6t-1 kCGMTY iklhnl-0 eEewhk"]' )
                hash.append(txhash.text)
                tstamp = ts.find_element(By.XPATH,'.//div[@class="kad8ah-0 fjudWa"]')
                timestamp.append(tstamp.text)
                val = ts.find_element(By.XPATH,'.//span[@class="sc-1ryi78w-0 cILyoi sc-16b9dsl-1 ZwupP u3ufsr-0 eQTRKC"]')
                value.append(val.text)
                opad = ts.find_element(By.XPATH,'.//div[@class="sc-19pxzmk-0 dVzTcW"]' )
                outputadd.append(opad.text[0:33])
        #if len(search)>50:
        dfi['transaction hash'] = hash
        dfi['timestamp'] = timestamp
        dfi['value'] = value
        dfi['o/paddress'] = outputadd
        dfi.to_csv(i+'.csv',index=False)



 

if __name__ == '__main__':
    main()