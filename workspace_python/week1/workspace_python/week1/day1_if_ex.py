
#조건1 : 학점 3.5이상
#조건2 : 봉사활동 50시간 초과
#사용자로부터 성적과 봉사활동 시간을 입력 받아 장학금
#지금 여부를 판단
#grade = float(input("성적을 입력하세요(0.0~4.5):"))
#hours = int(input("봉사활동 시간을 입력하세요:"))
#1,2조건을 만족하면 지금대상자 출력
#1만 만족하면 봉사 시간이 부족하여 대상자가 아닙니다 출력
#둘다 만족하지 않으면 성적이 부족하여 대상자가 아닙니다 출력


grade = float(input("성적을 입력하세요(0.0~4.5):"))
hours = int(input("봉사활동 시간을 입력하세요:"))
if grade >=3.5:
    if hours >50:
        print("장학금 대상자")
    else:
        print("봉사활동 시간 부족하여 장학금 대상자가 아닙니다")
else:
    print("성적이 부족하여 장학금 대상자가 아님")