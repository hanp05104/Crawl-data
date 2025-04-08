import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_vnexpress():
    url = 'https://vnexpress.net/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    articles = []

    for item in soup.select('article.item-news'):
        title_tag = item.select_one('h3.title-news a')
        if title_tag:
            title = title_tag.get_text(strip=True)
            link = title_tag['href']
            time_tag = item.select_one('span.time')
            time = time_tag.get_text(strip=True) if time_tag else 'N/A'

            articles.append({
                'title': title,
                'link': link,
                'time': time
            })

    # Lưu kết quả vào file Excel
    df = pd.DataFrame(articles)
    df.to_excel('vnexpress_news.xlsx', index=False)
    print(f'Đã crawl được {len(articles)} bài viết!')

if __name__ == '__main__':
    crawl_vnexpress()
