#환율 api
#USD1 달러 기준 각 국가의 환율 정보를 json 형태로 리턴함
#http://open.er-api.com/v6/latest/Usd
import requests

res = requests.get("http://open.er-api.com/v6/latest/Usd")
re_data = res.json()
exchange_rate = re_data['rates']['KRW'] #현재 환율


#원화 to 달러
krw_amount = float(input("원화 금액을 입력하세요!(원):"))
user_usd = krw_amount / exchange_rate
print(f"환율:1달러당 {exchange_rate:.2f}원 입니다.")
print(f"{user_usd: .2f}달러 입니다.")


#달러 to 원화
user_krw = user_usd * exchange_rate
print(f"환산된 원화 금액:{user_krw:.2f}원 입니다.")









