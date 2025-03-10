import urllib.request as req

url= 'https://img.cgv.co.kr/Movie/Thumbnail/Poster/000078/78085/78085_320.jpg'
req.urlretrieve(url,'test.png')