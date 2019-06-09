import json

from django.core.management.base import BaseCommand
from auctions.models import PgeAuction


class Command(BaseCommand):
    help = "loads json to database"

    def handle(self, *args, **options):
        json_data = open('/home/piotr/PycharmProjects/final_project/mysite/auction_scrapers/pge.json')
        json_loaded = json.load(json_data)
        for el in json_loaded:
            if isinstance(el["auction_number"], str):
                auction = PgeAuction()
                auction.auction_number = el["auction_number"]
                auction.auction_title = el["auction_title"]
                auction.auction_date_open = el["auction_date_open"][0]
                auction.auction_date_put = el["auction_date_put"][0]
                auction.auction_date_publish = el["auction_date_publish"][0]
                auction.save()

            else:
                print("Dupa coś nie działa")
