import random

#빈 SET 생성
lotto_num = set()
print(type(lotto_num))

#1 ~ 45사이의 랜덤 정수생성

#while문을 사용하여 1 ~ 45 사이의
# 중복되지 않은 6개 숫자를 생성하여 출력하시오
lotto_num = set()
print(type(lotto_num))
while len(lotto_num) < 6:
    lotto_num.add(random.randint(1,45))
print(sorted(lotto_num)) #sorted는 정렬 오름차순




#문제 2
#사용자에게 입력받은 수 만큼 로또 번호 생성
#3.  <--로또 번호 {6개} ,{6개},{6} (출력만)  --3을 입력시 3번 로또 번호가 나오게
cnt = int(input("몇개 생성할까요"))
print(("=" * 20) + "로또 생성" + ("=" * 20))
for i in range(cnt):
    user_lotto =set()
    while len(user_lotto) < 6:
        user_lotto.add(random.randint(1,45))
    print(user_lotto)
print(("=" * 20) + "생성 완료" + ("=" * 20))