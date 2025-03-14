import cx_Oracle

# Oracle DB 연결
conn = cx_Oracle.connect("member", "member", "localhost:1521/xe")
print("DB 연결 성공, 버전:", conn.version)

# SQL 쿼리 작성
sql = """
    SELECT *
    FROM member
    WHERE mem_name LIKE '%' || :1 || '%'
"""

# 커서 생성
cur = conn.cursor()

# SQL 실행 후 결과 가져오기
cur.execute(sql, ['은'])  # '은'이 포함된 사람 찾기
rows = cur.fetchall()  # ✅ fetchall() 추가

# 결과 출력
for row in rows:
    print(row)

# 연결 닫기
cur.close()
conn.close()
