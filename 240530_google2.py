from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import urllib.request
import os

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

#이미지 저장 폴더 생성
save_dir = "s_images" # 만들 폴더 이름 지정
os.makedirs(save_dir,exist_ok=True) # 폴더 생성, 이미 존재하면 무시 // # 폴더를 만든다 - make dir s , exist_ok=True >> 이미 존재하면 무시

driver = webdriver.Chrome(options=chrome_options)
URL = "http://www.google.com"
driver.get(URL) # 검색어를 포함한 URL로 이동

keyword="고양이 무료 png"
search_box = driver.find_element(By.ID, "APjFqb")
search_box. send_keys(keyword)
search_box. submit()
time. sleep(1)

#이미지 탭 클릭
driver.find_element(By.LINK_TEXT,"이미지"). click()
time.sleep(1)
####################
# 이미지 검색 개수 및 다운로드
links = []
images = driver.find_elements(By.CSS_SELECTOR,"g-img.mNsIhb>img.YQ4gaf") # CSS_SELECTOR : 특정 태그의 요소를 전부 가져옴
# print(images[0].get_attribute('src'))
# print(len(images))
for img in images:
    if img.get_attribute('src') != None:
        links.append(img.get_attribute('src'))

print("이미지 개수:",len(links))
# time.sleep(2)

# 이미지 저장(다운로드)
for i, u in enumerate(links):  # enumerate i와 u 에 인덱스와 값을 넣겠다 - 순서대로 번호를 매기기 위하여 인덱스를 넣어서 파일이름에 넣음
    urllib.request.urlretrieve(u,'./'+save_dir+'/cat_'+str(i)+'.jpg')

time.sleep(1)

print("완료")
driver.quit()

# url_img = images[0].get_attribute('src')
# urllib.request.urlretrieve(url_img,"test.jpg")

