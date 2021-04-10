# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Habitaclia2Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    titulo = scrapy.Field()
    precio = scrapy.Field()
    link = scrapy.Field()
    zona = scrapy.Field()
    ubicacion = scrapy.Field()
    m2 = scrapy.Field()
    habitaciones = scrapy.Field()
    baños = scrapy.Field()
    comentarios = scrapy.Field()
    detalles_generales = scrapy.Field()
    estadisticas = scrapy.Field()
    location = scrapy.Field()
    terraza = scrapy.Field()
    find_coords = scrapy.Field()
    coords = scrapy.Field()
    coordenadas = scrapy.Field()
    lat = scrapy.Field()
    lng = scrapy.Field()

