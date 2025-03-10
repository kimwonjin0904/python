from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time
import csv

def get_paxnset(page):
    url =f"https://www.hwahae.co.kr/rankings?english_name=category&theme_id={page}"
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    time.sleep(100)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    print(soup.prettify())

    #div = soup.select_one('hwahae-dataset')
    #div = soup.select_one('slick-list')
    div = soup.select_one('__next')
    lis = div.find_all('li')


    data_rows = []
    for i, li in enumerate(lis):
        if i != 0:
            seq = li.select_one('.type')
            if seq:
                seq_num = seq.get('data-seq')
                title = li.select_one('.title .best-title').text.strip()
                data_rows.append([seq_num, title])
    with open('paxnet.csv', 'a', encoding='utf-8', newline='') as f:
        write = csv.writer(f, delimiter='|')
        write.writerows(data_rows)


if __name__ == '__main__':
    for p in range(1, 11):
        get_paxnset(p)