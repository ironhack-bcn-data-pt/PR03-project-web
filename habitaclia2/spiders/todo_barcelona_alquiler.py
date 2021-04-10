import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider
import re

class TodoBarcelonaAlquilerSpider(CrawlSpider):

    name = 'todo_barcelona_alquiler'
    allowed_domains = ['www.habitaclia.com']
    start_urls = ['https://www.habitaclia.com/alquiler-barcelona.htm']
    rules = (
                Rule(LinkExtractor(allow=('https://www.habitaclia.com/alquiler-barcelona-'),),
                    callback='parse_item',
                    follow=True),
            )

    def parse_item(self, response):
        for article in response.xpath('/html/body/main/section/div/section[1]/article'):
            
            link_access = article.xpath('.//div/div/section[1]/h3/a/@href').extract()
            yield scrapy.Request(link_access[0], callback=self.parse_flat)


    def parse_flat(self, response):

        title = response.xpath('.//div/div/h1/text()[1]').get(default = "") + response.xpath('.//div/div/h1/text()[2]').get(default = "")
        zona = response.xpath('/html/body/main/div[1]/section[3]/div/div/article[1]/h4/a/text()').get()       
        price = response.xpath('.//div/div/div/span[@itemprop = "price"]/text()').get()
        m2 = response.xpath('.//div/div/article[2]/ul/li[1]/strong/text()').get()
        habitaciones = response.xpath('.//div/div/article[2]/ul/li[2]/strong/text()').get()
        baños = response.xpath('.//div/div/article[2]/ul/li[3]/strong/text()').get()
        parking = response.xpath('/html/body/main/div[1]/section[4]/div/article[4]/ul/li[contains(text(),"parking")]/text()').get()
        terraza = response.xpath('/html/body/main/div[1]/section[4]/div/article[3]/ul/li[contains(text(),"Terraza")]/text()').get()
        amueblado = response.xpath('/html/body/main/div[1]/section[4]/div/article[4]/ul/li[contains(text(),"Amueblado")]/text()').get()       
        find_coords = re.compile(r'VGPSLat.*?:(?P<lat>[\d\.]+),.*?VGPSLon.*?:(?P<lng>[\d\.]+)')
        coords = find_coords.search(response.xpath("/html/body/script[5]/text()").get())
        coordenadas = (coords.group('lat'), coords.group('lng'))
        lat = coordenadas[0]
        lng = coordenadas[1]
        link = response.url

        yield {"Título": title, "Zona": zona, "Precio": price, "M2": m2, "Habitaciones" : habitaciones, "Baños": baños, "Terraza": terraza, "Amueblado": amueblado, "Parking": parking, "Link" : link, "Latitud": lat, "Longitud": lng}

