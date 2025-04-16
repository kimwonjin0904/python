# pip install transformers torch
# pip install protobuf==3.20.*
from transformers import pipeline, BertTokenizer

analyzer = pipeline("sentiment-analysis")  # 오타 수정
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
comments = []  # 입력 문장 저장 리스트

while True:
    comment = input("감성 분석 문장 입력(종료:q): ")
    if comment.lower() == 'q':
        break
    tokens = tokenizer.tokenize(comment)
    if len(tokens) <= 512:  # 최대 토큰 길이 확인
        comments.append(comment)

# 감성 분석
sentiments = [analyzer(comment)[0]['label'] for comment in comments]

# 결과 집계
positive_cnt = sentiments.count("POSITIVE")
negative_cnt = sentiments.count("NEGATIVE")

print(f"긍정: {positive_cnt}개, 부정: {negative_cnt}개")
