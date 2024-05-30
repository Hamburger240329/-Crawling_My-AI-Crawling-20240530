from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 브라우저 꺼짐 방지 - 옵션설정
opt = Options()
opt.add_experimental_option('detach',True)

url = "https://www.naver.com"
# 크롬 드라이브 개체 생성
# driver = webdriver.Chrome()
driver = Chrome(options=opt)
driver.get(url)

#검색창에 키워드 입력 후 엔터
search_box = driver.find_element(By.ID,'query')
search_box.send_keys("멜론") # 검색창에 [인공지능] 글씨 넣기
search_box.send_keys(Keys.RETURN)  # 엔터 클릭
# 뉴스 탭 클릭
driver.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a/mark').click()

search_box2 = driver.find_element(By.ID,'top_search')
search_box2.send_keys("잔나비")
# search_box2.send_keys(Keys.RETURN)

