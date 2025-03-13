from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# APScheduler를 이용한 작업 함수
def test_interval():
    print("interval 실행")
    print(datetime.datetime.now())

def test_cron():
    print("cron 실행 ====================")
    print(datetime.datetime.now())

# 스케줄러 생성
workers = BlockingScheduler()

# 주기적으로 20초마다 실행
workers.add_job(test_interval, 'interval', seconds=20)

# 매일 15:35에 실행
workers.add_job(test_cron, 'cron', hour=15, minute=35)

# 매월 1일 오전 10시 30분 실행
workers.add_job(test_cron, 'cron', day=1, hour=10, minute=30)

# 월~금 오후 2시 실행 (0=월요일, 4=금요일)
workers.add_job(test_cron, 'cron', day_of_week='0-4', hour=14)

# 수요일과 금요일 오전 9시 실행 (2=수요일, 4=금요일)
workers.add_job(test_cron, 'cron', day_of_week='2,4', hour=9)

# 스케줄러 시작
workers.start()
