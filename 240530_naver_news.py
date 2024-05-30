import requests
import pandas as pd
from bs4 import BeautifulSoup
import json

#['259','260','258'] - for 문 돌릴경우 변경되는 값들

url="https://news.naver.com/breakingnews/section/101/259"
header = {'user-agnet' : 'Mozilla/5.0'}
res = requests.get(url,headers=header)
soup = BeautifulSoup(res.text,'lxml')

# print(soup)
#뉴스 제목과 링크 주소 가져오기
new_list=[]
teg3=soup.find('ul',{'class':'sa_list'}).find_all('li',limit=3)
for li in teg3:
    new_info={"title":li.find('strong',{'class':'sa_text_strong'}).text,
              "news_url":li.find('a')['href']
              }
    new_list.append(new_info)

#뉴스 상세페이지로 이동
# print(new_list)

for new in new_list:
    de_url = new['news_url']
    de_res = requests.get(de_url, headers=header)
    de_soup = BeautifulSoup(de_res.text, 'lxml')
    print(de_url)

    body = de_soup.find('article',{'class':'go_trans _article_content'})
    new_contents = body.text.replace("\n"," ").strip()
    new['news_contents'] = new_contents

df = pd.DataFrame(new_list)
# print(new_list)
# print(df)




# 한줄 요약하기

REST_API_KEY = '755db7074fd16e3654692c30afe1f466'

# KoGPT API 호출을 위한 메서드 선언
# 각 파라미터 기본값으로 설정
def kogpt_api(prompt, max_tokens = 1, temperature = 1.0, top_p = 1.0, n = 1):
    r = requests.post(
        'https://api.kakaobrain.com/v1/inference/kogpt/generation',
        json = {
            'prompt': prompt,
            'max_tokens': max_tokens,
            'temperature': temperature,
            'top_p': top_p,
            'n': n
        },
        headers = {
            'Authorization': 'KakaoAK ' + REST_API_KEY,
            'Content-Type': 'application/json'
        }
    )
    # 응답 JSON 형식으로 변환
    response = json.loads(r.content)
    return response

#KoGPT에게 전달할 명령어

# for i in range(1):  #len(df['news_contents'])
prompt = df['news_contents'].iloc[0]
print(prompt)
response = kogpt_api(prompt, max_tokens=128, top_p=0.7)
# print(response)
# summ = response['generations'][0]['text']
# print(summ)
    # # df['summary'].iloc[i]=summ


# print(df)


# for i in range(len(df['news_contents'])):
#     try:
#         prompt = df['news_contents'].iloc[i]
#         response = kogpt_api(prompt, max_tokens=128, top_p=0.7)
#         # print(response)
#         summ = response['generations'][0]['text']
#         df['summary'].iloc[i]=summ
#         # print(summ)
#     except:
#         pass
#
# print(df)