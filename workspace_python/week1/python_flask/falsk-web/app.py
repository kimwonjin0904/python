#pip install flask
from flask import Flask, request, render_template
import requests
import json
from flask_cors import CORS
app = Flask(__name__)
# 모든 요청 허용
# cross-origin resoutrce sharing 설정
CORS(app)

@app.route("/")
def index():
    return "hello, world"

@app.route("/main", methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        res = requests.get("https://api.upbit.com/v1/market/all")
        coin_list = json.loads(res.content)
        return render_template('main.html', coins=coin_list)
    else:
        data = request.get_json()
        res =  requests.get("https://api.upbit.con/v1/ticker?markets="+data['market'])
        return res.content

@app.route("/hello")
def hello():
    return render_template("hello.html", content="전달 내용", nm="pangsu")

if __name__ == '__main__':
    # app.run(debug=True)
    # host 설정 ip로 접근 가능
    app.run(debug=True, port=5500, host="0.0.0.0")
