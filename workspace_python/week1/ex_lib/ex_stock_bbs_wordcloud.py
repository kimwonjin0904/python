import pandas as pd
from week2.ex_db.DBManager import DBManager
sql = """
    SELECT *
    FROM stock_bbs
"""
db = DBManager()
conn = db.get_connection()
df = pd.read_sql(sql, conn)
for i, v in df.iterrows():
    print(v['BBS_CONTENTS'])
#1.명사 추출
#2.단어 카운트 생성
#3.워드클라우드 생성