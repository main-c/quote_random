import scrapy 

class QuotesSpider(scrapy.Spider):
    name = "authors"
    start_urls = [
        'https://citation-celebre.leparisien.fr/citation/vie',
    ]

    def parse(self, response):
        for author in response.css('div#citation_citationSearchList div.auteur'):
            yield {
                'author': author.css('a::text').extract_first(),
                }