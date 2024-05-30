import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_argument("headless")

# 검색어 입력
singer = input("검색할 가수 입력 >>> ")

# 드라이버 실행
driver = webdriver.Chrome(options=chrome_options)

# 웹주소 입력
url = 'https://www.melon.com/index.htm'
driver.get(url)

#검색창 찾기
elem = driver.find_element(By.ID, "top_search")
elem.clear()
# 검색어 입력
# elem.send_keys('잔나비')
elem.send_keys(singer)
elem.send_keys(Keys.RETURN)
time.sleep(2)

# '앨범' 메뉴을 xpath로 찾아 클릭 //*[@id="divCollection"]/ul/li[4]/a/span
album = driver.find_element(By.XPATH, '//*[@id="divCollection"]/ul/li[4]/a/span')
album.click()
time.sleep(2)
###############
#앨범 이미지를 xpath로 찾아 클릭
driver.find_element(By.XPATH,'//*[@id="frm"]/div/ul/li[1]/div/a[1]/span').click()
time.sleep(1)

lyrics=[]
stitle=[]
song_data = pd.DataFrame()
for i in range(1,5):
    try:
        #노래제목
        xp_t = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[4]/div/div/div[1]/span/a'
        song_title = driver.find_element(By.XPATH, xp_t).text
        stitle.append(song_title)

        #노래가사
        xp_s = f'//*[@id="frm"]/div/table/tbody/tr[{i}]/td[3]/div/a'
        driver.find_element(By.XPATH,xp_s).click() # 가사추출을 위해서 클릭함
        lyric = driver.find_element(By.ID,'d_video_summary').text.replace("\n"," ")
        lyrics.append(lyric)
        # print(song_title,lyric)

        driver.back() # 뒤로가기 코드
        time.sleep(1)
    except:
        pass
# print(stitle)
# print(lyrics)
song_data['노래제목'] = stitle
song_data['노래가사'] = lyrics
print(song_data)
# song_data.to_excel('잔나비노래.xlsx',engine='openpyxl')
song_data.to_excel(singer + '.xlsx',engine='openpyxl')
driver.quit()

