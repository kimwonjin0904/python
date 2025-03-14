import requests
import json

def get_bbs(code):
    url = f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}&size=100"
    res =requests.get(url)
    json_data = json.loads(res.text)
    for v in json_data['result']:
        print(v)
if __name__ == '__main__':
    get_bbs('069080')
# db 에서 krx_yn이 Y인 종목만 요청