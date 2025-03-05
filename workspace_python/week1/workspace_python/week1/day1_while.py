#while 조건식: 조건식이 True이면 반복
i = 1
while i <= 5:
    i += 1
    if i == 3:
        #continue #하위 내용을 건너뜀 계속 실행
        break #즉시 반복문 종료
    print(i)

flag = True
while flag:
    msg = input("종료(q):")
    if msg =='q':
        flag = False