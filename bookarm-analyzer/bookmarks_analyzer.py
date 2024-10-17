import os
from bs4 import BeautifulSoup

def extract_urls_from_bookmarks(file_path):
    urls = []
    if file_path.endswith('.html'):
        with open(file_path, 'r', encoding='utf-8') as file:
            soup = BeautifulSoup(file, 'html.parser')
            for a in soup.find_all('a', href=True):
                urls.append(a['href'])
    return urls

def categorize_url(url):
    video_patterns = ['youtube.com', 'vimeo.com', 'dailymotion.com']
    for pattern in video_patterns:
        if pattern in url:
            return 'video'
    return 'text'
