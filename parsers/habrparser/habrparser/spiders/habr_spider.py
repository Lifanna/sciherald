import scrapy


class HabrSpider(scrapy.Spider):
    name = "habr"

    def start_requests(self):
        urls = [
            'http://habr.com',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url

        categories = response.css("ul#navbar-links").extract()

        for category in response.css(".nav-links"):
            # yield{
            #     'link':annonce.css('::attr(href)').extract_first(),
            #     'title':annonce.css('.item_title::text').extract_first().strip(),
            #     }
            print("CATEGORY::::::       ", category.css('li').extract())

        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved file %s' % filename)
