import cx_Oracle
import logging

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class DBManager:
    def __init__(self):
        self.conn = None

    def get_connection(self):
        """DB 연결을 생성하여 반환"""
        try:
            if self.conn is None:
                self.conn = cx_Oracle.connect("member", "member", "localhost:1521/xe")
                logging.info("데이터베이스 연결 성공")
            return self.conn
        except Exception as e:
            logging.error(f"DB 연결 오류: {e}")
            return None

    def __del__(self):
        """객체 소멸 시 연결 종료"""
        if self.conn:
            self.conn.close()
            logging.info("DB 연결이 정상적으로 종료되었습니다.")

    def insert(self, query, param):
        """데이터 삽입"""
        cursor = None
        try:
            if self.conn is None:
                self.get_connection()
            cursor = self.conn.cursor()
            cursor.execute(query, param)
            self.conn.commit()
            logging.info("데이터 저장 완료!")
        except Exception as e:
            logging.error(f"저장 오류: {e}")
            if self.conn:
                self.conn.rollback()
        finally:
            if cursor:
                cursor.close()

if __name__ == '__main__':
    db = DBManager()
    conn = db.get_connection()
    if conn:
        db.insert("INSERT INTO 학생 (학번, 이름) VALUES(:1, :2)", [1, "동수"])
