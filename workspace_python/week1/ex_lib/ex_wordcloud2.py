# 필요한 라이브러리 임포트
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from konlpy.tag import Okt  # Okt() 불러오기
from collections import Counter

# CSV 파일 읽기
df = pd.read_csv("../../dataset/Ts/연예_E_TRAIN.csv", encoding="utf-8")
df_23 = df[df['PUBDATE'].astype(str).str.startswith("2023")]


# 데이터 크기 확인
print("데이터 크기:", df.shape)
print(df_23.shape)
# 형태소 분석기 객체 생성
okt = Okt()
nouns =[]
stop_words = {"개봉","앨범","통해","지난","오후","이번","기록","발매","차트"} #제외 단어 목록
# 형태소 분석 수행
for idx, row in df.iterrows():
    text = row['DATA_TEXT'].strip()
    word_list = okt.nouns(text)  # 명사만 추출
    filter_list = [x for x in word_list if len(x) > 1 and x not in stop_words]  #길이가 한개 보다 긴 단어만 추출
    nouns += filter_list
count = Counter(nouns)
print(count)


#워드 클라우드 생성
cloud = WordCloud(
    font_path="../../dataset/NanumGothicBold.ttf",  # 폰트 경로 확인 필수
    width=800, height=400, background_color="white")
gen =cloud.generate_from_frequencies(count)

# 시각화
plt.figure(figsize=(10, 5))
plt.imshow(cloud)
plt.axis("off")
plt.show()
