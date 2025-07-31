import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

class ScrapDetik:
    def __init__(self):
        self.search_url = 'https://www.detik.com/search/searchnews?'
    
    def build_search_url(self, query: str, result_type: str, page_number: int):
        if page_number == 1:
            return f"{self.search_url}query={query}&result_type={result_type}"
        else:
            return f"{self.search_url}query={query}&page={page_number}&result_type={result_type}"
    
    def scraping_articles(self, query: str, result_type: str, max_pages: int, name_file: str):
        data = []

        for page in range(1, max_pages+1):
            url = self.build_search_url(query, result_type, page)

            #Req URL
            page = requests.get(url)

            soup = bs(page.text, 'html.parser')

            article = soup.find_all('article')

            for scraping in article:
                try:
                    link = scraping.find("a", {"dtr-act": "artikel berita"})["href"]

                    article_page = requests.get(link)
                    article_soup = bs(article_page.text, 'html.parser')
                    title = scraping.find('h3', class_='media__title').text
                    print(title)
                    div_time_tag = scraping.find('div', class_='media__date')

                    if div_time_tag:
                        span_tag = div_time_tag.find('span')
                        # Pastikan elemen 'span' ditemukan sebelum mengakses atribut 'title'
                        if span_tag:
                            time = span_tag.get('title')
                            print(time)
                        else:
                            print("Tag 'span' tidak ditemukan di dalam 'div'.")
                    else:
                        print("Tag 'div' dengan class 'media__date' tidak ditemukan.")
                    print('='*10, '\n')

                    try:
                        # Coba mencari paragraf dengan struktur pertama
                        paragraphs = article_soup.find('div', class_='detail__body-text itp_bodycontent').find_all('p')
                        clean_paragraphs = [paragraph.get_text() for paragraph in paragraphs]
                    except AttributeError:
                        try :
                            paragraphs = article_soup.find('div', class_='detail__body-text').find_all('p')
                            clean_paragraphs = [paragraph.get_text() for paragraph in paragraphs]
                        except AttributeError:
                            clean_paragraphs = 'null'

                    data.append([title, link, time, clean_paragraphs, 'Non-Hoax'])
                except:
                    title = 'null'
                    link = 'null'
                    time = 'null'
                    clean_paragraphs = 'null'
                    
                    data.append([title, link, time, clean_paragraphs, 'Non-Hoax'])

        df = pd.DataFrame(data, columns=["Title", "Link", "Time", 'Narasi', 'Klasifikasi Berita'])

        df.to_csv(f'{name_file}.csv', index=False)
        return df