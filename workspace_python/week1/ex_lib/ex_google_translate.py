#pip install googletrans==4.0.0-rc1
#google 비공식 api 무료, 정책 변화에 따라 불안정 할 수 있음
#대량 번역시 IP차단될 수 있음(text크기 상황에따라)
#oliama
             #영어를 한국어로 번역!!#
from googletrans import Translator
# 한국:ko, 일본:ja, 프랑스:fr, 독일de, 영어:en
translator = Translator()

while True:
    message = input("번역! 영어를 입력하세요")
    result = translator.translate(message,src='en',dest='ko')
    print(result.text)