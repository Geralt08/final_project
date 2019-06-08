import scrapy




class AuctionTauronSpider(scrapy.Spider):
    name = "tauron"
    start_urls = [
        'https://swoz.tauron.pl/platform/HomeServlet?MP_module=main&MP_action=rfx_and_demand_notices&type=RfxAndDemandNotices&doSearch=true&org=000000010003',
    ]

    def parse(self, response):
        for auction in response.css('tr::attr(onmouseover)'):
            rv = {"auction_number": auction.xpath('./td[4]::text()').re(r'\d{4}.*'),
                  "auction_title": auction.xpath('td[1]//text()').re(r'.*'),
                  "auction_kind": auction.xpath('td[2]//text()').get(),
                  "auction_date_put": auction.xpath('td[3]//text()').get(),
                  "auction_date_open": auction.xpath('td[5]::text()').re(r'\d{4}-\d{2}-\d{2}')}
            yield rv

