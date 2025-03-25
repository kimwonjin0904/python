import requests

# data = {
#     "COMM_CD": "JB10",
#     "COMM_NM": "IT",
#     "COMM_PARENT": "JB00"
# }

# res = requests.post("http://localhost:5000/codes", json=data)
# print("post 응답:", res.json())

#data = {  "COMM_NM": "DB" }

# 'PUT' 요청으로 변경
#res = requests.put("http://localhost:5000/codes/JB07", json=data)
#print("put 응답:", res.json())

#delete
import requests

# 'DELETE' 요청으로 변경
res = requests.delete("http://localhost:5000/codes/JB09")
print("delete 응답:", res.json())
