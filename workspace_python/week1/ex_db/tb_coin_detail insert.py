import sqlite3
conn = sqlite3. connect("mydb.db")
 #1.array or tuple 순서로
sql = """
    INSERT INTO tb_coin_detail VALUES(?,?,?)       
"""
 #2.dict 키로 맵핑
sql2 = """
     INSERT INTO tb_coin_detail VALUES(:market, :price, :update_date)   
"""
data = {
    "market" : "마켓코드", "price": "가격", "update_date":"수집시간"
}
cur = conn.cursor()
cur.execute(sql, ['TEST','TEST,','TEST'])
cur.execute(sql2,data)
conn.commit()
conn.close()
