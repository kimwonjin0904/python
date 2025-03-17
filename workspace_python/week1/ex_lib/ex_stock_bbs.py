import requests
import json
import pandas as pd
from week1.test2 import main_url
from week2.ex_db.DBManager import DBManager

# DB에서 krx_yn이 'Y'인 종목만 요청
db = DBManager()


sql_merge = """
    MERGE INTO stock_bbs a
    USING DUAL
    ON (a.rsno = :rsno
       AND a.discussion_id = :discussion_id
       AND a.item_code = :item_code)
    WHEN MATCHED THEN
        UPDATE SET a.read_count = :read_count,
                   a.good_count = :good_count,
                   a.bad_count = :bad_count,
                   a.comment_count = :comment_count,
                   a.update_date = SYSDATE
    WHEN NOT MATCHED THEN  
        INSERT ( rsno,  discussion_id,  item_code,  title,  bbs_contents,  writer_id,
                read_count,  good_count,  bad_count,   comment_count,  end_path, update_date)
        VALUES (:rsno, :discussion_id, :item_code, :title, :bbs_contents, :writer_id,
                :read_count, :good_count, :bad_count, :comment_count, :end_path, 
                TO_DATE(:update_date, 'YYYY-MM-DD HH24:MI:ss'))
"""


def get_bbs(code):
    url = f"https://m.stock.naver.com/front-api/discuss?discussionType=localStock&itemCode={code}&size=100"
    res = requests.get(url)
    json_data = json.loads(res.text)

    for v in json_data['result']:
        row = {
            "rsno": v["rsno"],
            "discussion_id": v["discussionId"],
            "item_code": v["itemCode"],
            "title": v["title"],
            "bbs_contents": v["contents"][:1300],
            "writer_id": v["writerId"],
            "read_count": v["readCount"],
            "good_count": v["goodCount"],
            "bad_count": v["badCount"],
            "comment_count": v["commentCount"],
            "end_path": v["endPath"],
            "update_date": v["date"][:19]
        }

        try:
            db.insert(sql_merge, row)
        except Exception as e:
            print(str(e))
            print(row)


if __name__ == '__main__':
    conn = db.get_connection()

    selec_sql = """
        SELECT krx_code, krx_name, krx_market
        FROM tb_krx
        WHERE krx_yn = 'Y'
    """
    df = pd.read_sql(con=conn, sql=selec_sql)
    for i, v in df.iterrows():
        code = v['KRX_CODE']
        get_bbs(code)
        print("완료")
