#없다면 pip install requests
#http 요청을 쉽게 할 수 있는 라이브러리
#get,post,put,delete 요청처리
#응답 : json or text
#요청시 자동으로 URL 인코딩 처리
#http 요청중 발생할 수 있는 오류에 대한 예외처리 제공
import requests

url = "https://api.upbit.com/v1/market/all"
res = requests.get(url)
if res.status_code == 200:
    data = res.json()  # 응답을 JSON 형식으로 변환
    for v in data:  # JSON 데이터를 순회하며 출력
        print(v['market'])
        print(f"마켓명:{v['market'     ]}"
              f"코인명:{v['korean_name']}")




import requests  # requests 모듈 import

def fn_get_coin_price(code):
    """
    업비트 API를 이용하여 특정 코인의 실시간 거래 가격을 반환하는 함수
    :param code: 코인 마켓 코드 (예: "KRW-BTC")
    :return: price (거래 가격)
    """
    url = f"https://api.upbit.com/v1/ticker?markets={code}"
    res = requests.get(url)
    price = 0  # 기본값 설정

    if res.status_code == 200:
        data = res.json()
        price = data[0]['trade_price']
    return price
print("KRW-BTC:", fn_get_coin_price("KRW-BTC"))
print("KRW-ETH:", fn_get_coin_price("KRW-ETH"))
