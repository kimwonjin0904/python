from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # 자동 설치
import csv
import time


def get_product_reviews(product_url, driver):
    """제품 상세 페이지에서 리뷰 크롤링"""
    reviews = []

    try:
        driver.get(product_url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".review-list")))

        # BeautifulSoup로 HTML 파싱
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 리뷰 리스트 가져오기
        review_elements = soup.select(".review-list .review-text")

        for review in review_elements:
            text = review.text.strip()
            if text:
                reviews.append(text)

    except Exception as e:
        print(f"리뷰 크롤링 오류 발생: {e}")

    return reviews


def get_hwahae(page, driver):
    """화해 제품 랭킹 페이지 크롤링 + 리뷰 가져오기"""
    url = f"https://www.hwahae.co.kr/rankings?english_name=category&theme_id={page}"

    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "ul")))
        time.sleep(3)  # 추가 대기

        # BeautifulSoup로 HTML 파싱
        soup = BeautifulSoup(driver.page_source, "html.parser")

        # 제품 리스트 찾기
        data_rows = []
        for item in soup.select("li"):  # 각 제품 리스트 아이템
            title_element = item.select_one(".title .best-title")
            link_element = item.select_one("a")  # 제품 상세 페이지 링크

            if title_element and link_element:
                title = title_element.text.strip()
                product_url = "https://www.hwahae.co.kr" + link_element["href"]

                # 상세 페이지에서 리뷰 가져오기
                reviews = get_product_reviews(product_url, driver)
                reviews_text = " | ".join(reviews[:5])  # 리뷰 5개까지만 저장

                data_rows.append([title, product_url, reviews_text])

        # CSV 파일 저장
        with open("hwahae_reviews.csv", "a", encoding="utf-8", newline="") as f:
            writer = csv.writer(f, delimiter="|")
            writer.writerows(data_rows)

    except Exception as e:
        print(f"오류 발생: {e}")
        time.sleep(5)  # 오류 발생 시 대기 후 재시도 가능


def main():
    """크롤링 실행"""
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 💡 브라우저 숨기기 (필요시 활성화)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("window-size=1920x1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # WebDriver 실행 (자동 설치)
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        })
        driver.execute_cdp_cmd("Network.enable", {})

        headers = {
            "Accept-Language": "ko-KR,ko;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.google.com/",
            "DNT": "1",
            "Upgrade-Insecure-Requests": "1"
        }
        driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": headers})

        # 크롤링 실행 (1~3페이지)
        for p in range(1, 4):
            get_hwahae(p, driver)
            time.sleep(2)  # 페이지 전환 시 대기

    finally:
        driver.quit()  # 실행 후 안전하게 종료


if __name__ == "__main__":
    main()
