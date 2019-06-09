from django.db import models

# Create your models here.
class PgeAuction(models.Model):
    auction_number = models.CharField(max_length=32)
    auction_title = models.CharField(max_length=400)
    auction_date_publish = models.CharField(max_length=32)
    auction_date_put = models.CharField(max_length=32)
    auction_date_open = models.CharField(max_length=32)



