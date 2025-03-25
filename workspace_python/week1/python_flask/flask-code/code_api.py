from flask import Flask, request, jsonify
import cx_Oracle

app = Flask(__name__)

# Oracle 연결
try:
    conn = cx_Oracle.connect("jdbc", "jdbc", "localhost:1521/xe")
    cur = conn.cursor()
except cx_Oracle.DatabaseError as e:
    print(f"Database connection error: {e}")

# /codes : GET 조회
@app.route("/codes", methods=['GET'])
def get_codes():
    try:
        cur.execute("SELECT COMM_CD, COMM_NM, COMM_PARENT FROM COMM_CODE")
        rows = cur.fetchall()

        # 컬럼 가져오기
        columns = [col[0] for col in cur.description]

        # 딕셔너리로 변환
        results = [dict(zip(columns, row)) for row in rows]

        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# /codes : POST 저장
@app.route("/codes", methods=['POST'])
def insert_code():
    data = request.get_json()

    # 필수 필드 확인
    cd = data.get('COMM_CD')
    nm = data.get('COMM_NM')
    parent = data.get('COMM_PARENT', None)  # COMM_PARENT가 없으면 기본값 None

    if not cd or not nm:
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        sql = "INSERT INTO COMM_CODE (COMM_CD, COMM_NM, COMM_PARENT) VALUES (:1, :2, :3)"
        cur.execute(sql, [cd, nm, parent])
        conn.commit()
        return jsonify({'message': 'Insert success'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# /codes/<comm_cd> : PUT 수정
@app.route("/codes/<comm_cd>", methods=['PUT'])
def update_codes(comm_cd):
    data = request.get_json()
    nm = data.get('COMM_NM')

    if not nm:
        return jsonify({'error': 'COMM_NM is missing'}), 400  # 더 구체적인 오류 메시지

    try:
        sql = """UPDATE COMM_CODE
                 SET COMM_NM = :1
                 WHERE COMM_CD = :2
        """
        cur.execute(sql, [nm, comm_cd])
        if cur.rowcount == 0:
            return jsonify({'error': f'cd: {comm_cd} not found'}), 404  # 해당 COMM_CD가 없을 경우 처리
        conn.commit()
        return jsonify({'message': 'update!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# /codes/<comm_cd> : DELETE 삭제
@app.route("/codes/<comm_cd>", methods=['DELETE'])
def delete_codes(comm_cd):
    try:
        sql = """DELETE FROM COMM_CODE WHERE COMM_CD = :1"""
        cur.execute(sql, [comm_cd])
        if cur.rowcount == 0:
            return jsonify({'error': f'cd: {comm_cd} not found'}), 404  # 해당 COMM_CD가 없을 경우 처리
        conn.commit()
        return jsonify({'message': 'delete success'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
