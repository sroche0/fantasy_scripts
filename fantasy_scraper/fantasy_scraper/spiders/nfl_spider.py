__author__ = 'sroche'
import scrapy

class NflSpider(scrapy.Spider):
    name = "nfl_game_stats"
    allowed_domains = ["nfl.com"]
    start_urls = [
        "http://fantasy.nfl.com/league/1163074/team/9/gamecenter?gameCenterTab=preview&previewType=sbs&week=1",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
