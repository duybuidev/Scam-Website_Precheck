# scraper.py

import requests
from bs4 import BeautifulSoup

def get_page_content(url):
    """
    Gửi request với header User-Agent để giả lập trình duyệt.
    """
    # Thêm header User-Agent để giả lập trình duyệt
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Gây lỗi nếu HTTP status code là 4xx hoặc 5xx
        return BeautifulSoup(response.text, 'html.parser')
    except requests.exceptions.RequestException as e:
        print(f"Lỗi khi lấy dữ liệu từ {url}: {e}")
        return None


def extract_links(soup):
    """
    Trích xuất tất cả các đường link từ đối tượng BeautifulSoup.
    """
    if soup:
        return [link.get('href') for link in soup.find_all('a') if link.get('href')]
    return []

def extract_titles(soup):
    """
    Trích xuất tất cả các tiêu đề h1 từ đối tượng BeautifulSoup.
    """
    if soup:
        return [h1.text for h1 in soup.find_all('h1')]
    return []
