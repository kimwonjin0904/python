#업다운 게임
#3번의 기회
#사용자 입력이  맞으면 '정답'
            # 작으면 '업'
            # 크면 '다운' 출력
#틀릴때 마다 몇 번의 기회가 있는지 출력
#computer의 랜덤 값은 1 ~10 사이의 정수
import random

print("업다운 게임!!!")
com = random.randint(1, 10)
cnt = 3
while cnt >0:
    user_num = int(input("1 ~ 10사이의 정수 입력"))
    if user_num < com:
        print("업!")
    elif user_num > com:
        print("다운")
    elif user_num == com:
        print("정답")
        break
    cnt -=1
    if cnt != 0:
        print("남은 기회:", cnt)
    else:
        print("다음기회에.,,")