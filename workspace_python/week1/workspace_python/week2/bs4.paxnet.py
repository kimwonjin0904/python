import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver

def get_paxnset(page):
    # 컨트롤 에프 검색기능
    url = f"https://www.paxnet.co.kr/tbbs/list?tbbsType=L&id=N10841&page={page}"
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    print(soup.prettify())
    #id:comm-list
    #dml li 출력
    div = soup.select_one('#comm-list')
    lis = div.find_all('li')

    data_rows = []
    for i, li in enumerate(lis):
        if i !=0:
          seq = li.select_one('.type')
          if seq:
              seq_num = seq.get('data-seq')
              title = li.select_one('.title .best-title').text.strip()
              data_rows.append([seq_num, title])
    with open('paxnet.csv', 'a', encoding='utf-8', newline='' ) as f:
        write = csv.writer(f, delimiter='|')
        write.writerows(data_rows)

if __name__=='__main__':
    for p in range(1, 11):
        get_paxnset(p)