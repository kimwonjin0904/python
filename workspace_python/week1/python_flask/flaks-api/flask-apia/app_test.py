import requests

res = requests.get("http://localhost:5000/items")
print("get /items 테스트:", res.json())

res = requests.get("http://localhost:5000/items/1")
print("get /items/1 테스트:", res.json())

res = requests.get("http://localhost:5000/items/3")
if res.status_code == 200:
    print("get /items/3 테스트:", res.json())
else:
    print(f"get /items/3 테스트: 실패 (status: {res.status_code})")

data = {'name': 'melon', 'price': 6000}
res = requests.post("http://localhost:5000/items", json=data)
print("post 테스트:", res.json())

# PUT 요청: 올바른 item_id 추가
update_data = {'price': 2500}
res = requests.put("http://localhost:5000/items/1", json=update_data)  # 아이템 ID 명시
print("put 테스트:", res.json())

res = requests.put("http://localhost:5000/items/1", json=update_data)
print("delete 테스트:", res.json())

res =requests.get('http://localhost:5000/items')
print("now:" ,res.json())
