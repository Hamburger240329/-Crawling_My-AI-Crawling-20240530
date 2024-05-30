# from selenium import webdriver
from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # 태그를 찾기 위한 기능 import 함
from selenium.webdriver.common.keys import Keys  # 외부에서 사용자가 입력하는 조작을 하기위한 라이브러리

# 브라우저 꺼짐 방지 - 옵션설정
opt = Options()
opt.add_experimental_option('detach',True)
# opt.add_argument('headless')  # 웹브라우저를 띄우지 않고 진행하기 // 브라우저 실행되는 화면 안나옴

url = "https://www.naver.com"
# 크롬 드라이브 개체 생성
# driver = webdriver.Chrome()
driver = Chrome(options=opt)
driver.get(url)

#검색창에 키워드 입력 후 엔터
search_box = driver.find_element(By.ID,'query')
search_box.send_keys("인공지능") # 검색창에 [인공지능] 글씨 넣기
search_box.send_keys(Keys.RETURN)  # 엔터 클릭

# 뉴스 탭 클릭
# driver.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/div[1]/div/div[1]/div[3]/a').click()
driver.find_element(By.LINK_TEXT,'뉴스').click()
# time.sleep(3)

# 화면 스크롤 - body 안에서 스크롤 내리겠다 ~
scroll = driver.find_element(By.TAG_NAME,'body') # 전체 가 하나이기 때문에 element(단일) 사용
for i in range(60):
    scroll.send_keys(Keys.PAGE_DOWN) # 어느 영역에서 페이지 다운하겠다 - 바로 위에서 만들어줬음
    time.sleep(0.2)

# 뉴스 제목 텍스트 추출
new_titles = driver.find_elements(By.CLASS_NAME,"news_tit")
# print(new_titles[0].text)  # 텍스트 표시
# cn=1
# for i in new_titles:
#     print(cn,i.text)
#     cn+=1
cn=1
for i in new_titles:
    print(cn,"번째 저장중>>>>>>>>>")
    with open("news.csv",'a',encoding='UTF-8') as f:
        f.write(str(cn)+"."+i.text)
        f.write('\n')
        cn+=1

driver.quit()  # 메모리 안에서 없애기


