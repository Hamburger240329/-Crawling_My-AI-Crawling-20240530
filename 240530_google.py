import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 검색어 입력
singer = input("검색키워드 입력 >>> ")
driver = webdriver.Chrome(options=chrome_options)
url = 'https://www.google.co.kr'
driver.get(url)


