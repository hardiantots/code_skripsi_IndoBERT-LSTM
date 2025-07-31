from detik import ScrapDetik

# Detik
detik_scraping = ScrapDetik()
detik_news = detik_scraping.scraping_articles(query='pemerintahan', result_type='relevansi', max_pages=800, name_file='detik_pemerintahan1')

