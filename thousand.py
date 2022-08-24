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
    search100 = []
    df = pd.DataFrame()
    for i in inp_ad[0:500:5]:
        print(i)
        dfi = pd.DataFrame()
        hash = []
        timestamp = []
        value = []
        outputadd = []
        ts_url = 'https://www.blockchain.com/btc/address/' + i
        driver.get(ts_url)

        search = driver.find_elements(By.XPATH, './/div[@class="sc-8sty72-0 bFeqhe"]')
        tns = search[5]
        tnsi = int(tns.text)
        print(tnsi)
        if tnsi>99:
            search100.append(i)
    df['inp_address'] = search100
    df.to_csv('s100.csv',index = False)




 

if __name__ == '__main__':
    main()