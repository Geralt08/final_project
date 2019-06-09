from django import views
from django.shortcuts import render

import models


class MainView(views.View):
    def get(self, request):
        auctions = models.PgeAuction.objects.get.all()
        ctx = {"auctions": auctions}
        return render(request, 'main.html', ctx)
