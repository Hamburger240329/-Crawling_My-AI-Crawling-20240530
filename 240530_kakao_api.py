import requests
import json

#다음(daum) 검색
url='https://dapi.kakao.com/v2/search/web'
# 위나 아래 둘중 하나의 방법으로 넣으주면 됨
# url_get = "https://dapi.kakao.com/v2/search/web?query=인공지능"

rest_api_key = '755db7074fd16e3654692c30afe1f466'
my_headers={"Authorization": "KakaoAK " + rest_api_key}
req_params = {'query' : '인공지능',
              'page' : 1,
              'size' : 10,
              'sort' : 'accuracy'
}

r = requests.get(url,params=req_params,headers=my_headers)
# r = requests.get(url,headers=headers=my_headers)

# print(r.status_code)
# print(r['documents'])
result = r.json()
print(len(result['documents']))
for i in range(1,10):
    print(i,result['documents'][i]['contents'])

# print(result['documents'][2]['contents'])


