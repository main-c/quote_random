import scrapy 

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://citation-celebre.leparisien.fr/citation/vie',
    ]

    def parse(self, response):
        for quote in response.css('div#citation_citationSearchList div.laCitation'):
            yield {
                'quote': quote.css('a::text').extract_first(),
                }