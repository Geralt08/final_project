from django import views
from django.shortcuts import render

from auctions.models import PgeAuction


class MainView(views.View):
    def get(self, request):
        auctions = PgeAuction.objects.all()
        ctx = {"auctions": auctions}
        return render(request, 'main.html', ctx)
