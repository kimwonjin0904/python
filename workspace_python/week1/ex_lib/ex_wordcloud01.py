# 필요한 라이브러리 임포트
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# CSV 파일 읽기
df = pd.read_csv("../../dataset/Ts/스포츠_S_TRAIN.csv", encoding="utf-8")

# 데이터 합치기
text_data = " ".join(df['DATA_TEXT'].dropna())

# 워드 클라우드 생성
cloud = WordCloud(
    font_path="../../dataset/NanumGothicBold.ttf",  # 폰트 경로 확인 필수
    width=800, height=400, background_color="white"
).generate(text_data)

# 시각화
plt.figure(figsize=(10, 5))
plt.imshow(cloud)
plt.axis("off")
plt.show()
