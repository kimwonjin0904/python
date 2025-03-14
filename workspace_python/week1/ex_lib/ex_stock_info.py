import pandas as pd
from week2.ex_db.DBManager import DBManager
import cx_Oracle

# DB 연결
db = DBManager()

# 엑셀 읽어오기
krx_df = pd.read_excel("krx.xlsx", engine='openpyxl')

# SQL INSERT문 (올바른 문법 적용)
SQL = """
    INSERT INTO tb_krx (krx_code, krx_name, krx_market, krx_volume) 
    VALUES (:1, :2, :3, :4)
"""
print(krx_df.head())
for i, row in krx_df.iterrows():
    code = row['Code']
    nm = row['Name']
    market = row['Market']
    vol = row['Volume']
    print(f"{i}: {nm}-{code}-{market}-{vol}")
    db.insert(SQL, [code, nm, market, vol])  # 바인딩 변수 적용
print("종료")
