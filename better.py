import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import sys
import os

rti = []

def main():
    exe_path = 'chromedriverf/chromedriver'
    driver = webdriver.Chrome(exe_path)
    driver.implicitly_wait(0)
    df = pd.read_csv('InputAddress.csv')
    inp_ad = df['address'].values
    for i in inp_ad:
        ts_url = 'https://www.blockchain.com/btc/address/' + i
        driver.get(ts_url)
        tstamp = ts.find_element(By.XPATH,'.//div[@class="kad8ah-0 fjudWa"]')
        timestamp.append(tstamp.text)




 

if __name__ == '__main__':
    main()