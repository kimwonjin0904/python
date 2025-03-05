import random

import requests

from week1.day2_exchange import re_data, krw_amount, exchange_rate, user_usd


def get_lotto():
    """
    로또 번호 6개 생성
    1~45 사이의 숫자
    :return: set
    """
    lotto_num =set()
    while len(lotto_num) < 6:
        lotto_num.add(random.randint(1,45))
    return lotto_num






def krw_to_usd(krw):
    pass
    res = requests.get("http://open.er-api.com/v6/latest/Usd")
    re_data = res.json()
    exchange_rate = re_data['rates']['KRW'] # 현재 환율
    
def used_to_krw(usd):
    pass
    user_krw = user_usd * exchange_rate

# 원화 to 달러
#달러 to 원화 만들어주세요
test = (1, 14, 15)
#to list
test2 = list(test)[:2]
print(test2)
my_set = set(test2) #해당 데이터가 포함 되어있는 set 생성
print(my_set, type(my_set))

#user_lotto 함수 생성
#input : 0~n개 (사용자 희망 번호) 가변!?
#output: true or false, 메세지, 로도 번호(사용자 희망 번호가 포함된) 여러개!?
#사용 입력 번호를 포함 시켜서 로또 번호 생성
#단 사용자 입력은 최대 5개 깍지만 포함 슬라이싱!?
#각 사용자 입력은 1~45사이 수만
#조건을 만족 하지 않으면 false, 만족하면 true
#메세지는 false일대 false인지




#모듈내 실행
if __name__ == '__main__':  # 공백 추가 (if와 __name__ 사이)
    print("로또")
    print("dd")
    print(f"달리 100은 : {used_to_krw(100)}원" )
    print(f"원화 20000은: {krw_to_usd(20000)}달러")