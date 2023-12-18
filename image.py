from icrawler.builtin import GoogleImageCrawler


def imageSourcing(query):
    google_Crawler = GoogleImageCrawler(storage={'root_dir': r'Images'})
    google_Crawler.crawl(keyword=f'{query}', max_num=1)
