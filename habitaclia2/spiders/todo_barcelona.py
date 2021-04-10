import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider


class TodoBarcelonaSpider(CrawlSpider):
    name = 'todo_barcelona'
    allowed_domains = ['habitaclia.com']
    start_urls = ['https://www.habitaclia.com/viviendas-barcelona.htm']
    rules = (
                Rule(LinkExtractor(allow=('https://www.habitaclia.com/viviendas-barcelona-'),),
                    callback='parse_item',
                    follow=True),
            )

    def parse_item(self, response):
        for article in response.xpath('/html/body/main/section/div/section[1]/article'):
            
            link_access = article.xpath('.//div/div/section[1]/h3/a/@href').extract()
            yield scrapy.Request(link_access[0], callback=self.parse_flat)


    def parse_flat(self, response):
        title = response.xpath('.//div/div/h1/text()[1]').get(default = "") + response.xpath('.//div/div/h1/text()[2]').get(default = "")
        zona = response.xpath('.//div/div/section[1]/p[1]/span/text()').get()
        price = response.xpath('.//div/div/div/span[@itemprop = "price"]/text()').get()
        m2 = response.xpath('.//div/div/article[2]/ul/li[1]/strong/text()').get()
        habitaciones = response.xpath('.//div/div/article[2]/ul/li[2]/strong/text()').get()
        baños = response.xpath('.//div/div/article[2]/ul/li[3]/strong/text()').get()
        parking = response.xpath('//section[4]/div/article[3]/ul/li[contains(text(),"parking")]/text()').get()
        link = response.url

        yield {"Título": title, "Zona": zona, "Precio": price, "M2": m2, "Habitaciones" : habitaciones, "Baños": baños, "Parking": parking, "Link" : link}

