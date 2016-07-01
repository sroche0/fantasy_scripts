import scrapy

class DmozSpider(scrapy.Spider):
    name = "fantasy"
    allowed_domains = ["nfl.com"]
    start_urls = [
        "https://id2.s.nfl.com/fans/login?s=fantasy&returnTo=http%3A%2F%2Ffantasy.nfl.com%2Fleague%2F1163074"]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username': 'sroche0', 'password': '0vuWLLHz'},
            callback=self.after_login
        )

    def after_login(self, response):
        print '-' * 40
        print
        print response
        print
        print '-' * 40
        # check login succeed before going on
        if "Check username" in response.body:
            self.log("Login failed", level=log.ERROR)
            print 'FAIL'
            return