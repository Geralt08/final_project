# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# class AuctionScrapersItem(scrapy.Item):
#     define the fields for your item here like:
# name = scrapy.Field()
# pass
from scrapy_djangoitem import DjangoItem

from mysite.auctions.models import PgeAuction


class PgeItem(DjangoItem):
    django_model = PgeAuction

