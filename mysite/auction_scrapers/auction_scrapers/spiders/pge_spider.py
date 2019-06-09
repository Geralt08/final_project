import scrapy

# from auction_scrapers import items


class AuctionPgeSpider(scrapy.Spider):
    name = "pge"
    start_urls = [
        'https://pgedystrybucja.pl/przetargi',
    ]

    def parse(self, response):
        for auction in response.css('h4.panel-title'):
            rv = {"auction_number": auction.css('span.auction-number::text').get(),
                  "auction_title": auction.xpath('.//a/span/following-sibling::text()').get(),
                  "auction_date_publish": auction.css('span.auction-date-publish::text').re(
                      r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'),
                  "auction_date_put": auction.css('span.auction-date-put::text').re(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}'),
                  "auction_date_open": auction.css('span.auction-date-open::text').re(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}')}
            for k in rv:
                if isinstance(rv[k], str):
                    rv[k] = rv[k].strip()

            yield rv

            # item = items.PgeItem()
            # item["auction_number"] = rv["auction_number"]
            # item["auction_title"] = rv["auction_title"]
            # item["auction_date_publish"] = rv["auction_date_publish"]
            # item["auction_date_put"] = rv["auction_date_put"]
            # item["auction_date_open"] = rv["auction_date_open"]
            # yield item


