#반복문
arr = ['팽수', '길동', '동길']
#방법1. 값만 필요 할때
for v in arr:
    print(v)

#방법2. 값, 인덱스 둘다 필요 할때
for i, v in enumerate(arr):
    print(i,v)

#방법3.단수 횟수 반복
for i in range(3):
    print(i)

for i in range(len(arr)):
    print(arr[i])

for i in range(1,4):    #1부터 1씩증가
    print(i)

for i in range(2,11,2): #2부터 2씩 증가
    print(i)



