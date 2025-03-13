import sqlite3
import requests
import json
import datetime

# SQLite 데이터베이스 연결
conn = sqlite3.connect('mydb.db')
cur = conn.cursor()

# 테이블 생성 (이미 존재하면 생성 안 함)
sql_create = """
     CREATE TABLE IF NOT EXISTS tb_coin_detail (
          market TEXT,
          price TEXT,
          update_date TEXT
     )
"""
cur.execute(sql_create)

# tb_coin 테이블에서 데이터 조회
cur.execute("SELECT * FROM tb_coin")
rows = cur.fetchall()  # 커서 데이터를 한 번에 가져오기

# 현재 시간 포맷
now = datetime.datetime.now()
format_now = now.strftime("%Y-%m-%d %H:%M:%S")

for row in rows:
    market = row[0]
    kr_nm = row[1]
    print(market, kr_nm)

    # Upbit API 호출
    url = f"https://api.upbit.com/v1/ticker?markets={market}"
    res = requests.get(url)

    if res.status_code == 200:
        json_data = json.loads(res.text)[0]
        price = "{:.15f}".format(json_data['trade_price'])  # 가격을 문자열로 변환
        print(market, kr_nm, price, format_now)

        # 데이터 삽입 SQL
        sql_insert = "INSERT INTO tb_coin_detail (market, price, update_date) VALUES (?, ?, ?)"
        cur.execute(sql_insert, (market, price, format_now))

# 트랜잭션 커밋
conn.commit()

# 연결 종료
conn.close()
