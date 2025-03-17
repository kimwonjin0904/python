# 필요한 라이브러리 임포트 하트모양안됨
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt  # Okt() 불러오기
from collections import Counter
from PIL import Image
import numpy as np

# CSV 파일 읽기
df = pd.read_csv("../../dataset/Ts/연예_E_TRAIN.csv", encoding="utf-8")

# 2023년 데이터 필터링
df_23 = df[df['PUBDATE'].astype(str).str.startswith("2023")]

# 데이터 크기 확인
print("전체 데이터 크기:", df.shape)
print("2023년 데이터 크기:", df_23.shape)

# 형태소 분석기 객체 생성
okt = Okt()
nouns = []

# 마스크 이미지 로드 (경로 수정)
icon = Image.open("../../dataset/heart.png").convert("RGBA")  # RGBA 변환
mask = np.array(icon)

# 흰색 배경을 255로 변환 (마스크가 적용되도록)
mask = np.where(mask[:, :, 3] == 0, 255, mask[:, :, 0])  #
# 제외할 단어 목록
stop_words = {"개봉", "앨범", "통해", "지난", "오후", "이번", "기록", "발매", "차트"}

# 형태소 분석 수행 (2023년 데이터만 분석)
for idx, row in df_23.iterrows():
    text = row['DATA_TEXT']

    # NaN 방지 및 문자열 변환 후 처리
    if pd.notna(text):
        text = str(text).strip()
        word_list = okt.nouns(text)  # 명사만 추출
        filter_list = [x for x in word_list if len(x) > 1 and x not in stop_words]  # 한 글자 이상 & 제외 단어 필터링
        nouns += filter_list

# 단어 빈도수 계산
count = Counter(nouns)
print(count.most_common(20))  # 상위 20개 단어 출력

# 워드 클라우드 생성
cloud = WordCloud(
    font_path="../../dataset/NanumGothicBold.ttf",
    width=800, height=400, background_color="white",
    mask=mask, contour_color="black",
    min_font_size=15) #최소 폰트 크기
gen = cloud.generate_from_frequencies(count)

# 시각화
plt.figure(figsize=(10, 5))
plt.imshow(cloud, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
