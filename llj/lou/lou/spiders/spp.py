import scrapy

class Spiderlou (scrapy.Spider):
    name = "palou"
    start_urls = [
        "http://www.19lou.com"
    ]

    def parse (self, response):
        print response.body
