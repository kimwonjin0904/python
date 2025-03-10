from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

url = 'https://www.melon.com/chart/index.htm'
#406상황
#res = requests.get(url)
#print(res.status_code)
#soup = BeautifulSoup(res.content, 'html.parser')
#print(soup.prettify())

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.get(url)
time.sleep(1)
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()
print(soup.prettify())

tbody = soup.find('tbody')
trs = tbody.find_all('tr')
for tr in trs:
    print(tr)
    tds = tr.find_all('td')
    rank = tds[2].select_one('span.rank').text
    a_tags = tds[5].find_all('a')
    title = a_tags[0].text
    singer = a_tags[1].text
    print(rank)
    print("=" * 100)