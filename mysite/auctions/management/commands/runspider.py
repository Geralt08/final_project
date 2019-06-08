import pprint
import sys

pprint.pprint(sys.path)

from django.core.management.base import BaseCommand
from auction_scrapers.auction_scrapers.spiders.pge_spider import AuctionPgeSpider
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class Command(BaseCommand):
    help = "Release the spiders"

    def handle(self, *args, **options):
        process = CrawlerProcess(get_project_settings())

        process.crawl(AuctionPgeSpider)
        process.start()
