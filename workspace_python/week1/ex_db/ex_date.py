import  datetime
now =datetime.datetime.now()
print("현재 날짜와 시간",now)    #현재 날짜와 시간 2025-03-12 15:22:10.871689
#format to string
format_now = now.strftime("%Y-%m-%d %H:%M:%S")
print(format_now)     #2025-03-12 15:22:10
format_now2 = now.strftime("%y-%m-%d %H %M %S")
print(format_now2) #대소문자 표현이 다름   #25-03-12 15 22 10
time_now = now.timestamp()
print(time_now)        #1741760530.871689
time_to_date = datetime.datetime.fromtimestamp(time_now).strftime("%Y-%m-%d")
print(time_to_date)             #2025-03-12
#문자열 to 데이트타임
date_str = "2025-01-17 09:10:00"
start_date = datetime.datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")
print(start_date, type(start_date))         #2025-01-17 09:10:00 <class 'datetime.datetime'>
#특정 날짜와 시간
dday = datetime.datetime(2025,7,12,17,50)   #출력결과: 2025-07-12 17:50:00
print(dday)
#오늘 날짜만
today = datetime.date.today()
print(today)