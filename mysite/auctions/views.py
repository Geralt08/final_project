from django import views
from django.shortcuts import render

from auctions.models import PgeAuction


class IndexView(views.View):
    def get(self, request):
        return render(request, 'index.html', )


class PgeView(views.View):
    def get(self, request):
        auctions = PgeAuction.objects.all()
        ctx = {"auctions": auctions}
        return render(request, 'pge.html', ctx)

class TauronView(views.View):
    def get(self, request):
        return render(request, 'tauron.html', )

class EneaView(views.View):
    def get(self, request):
        return render(request, 'enea.html', )

class EnergaView(views.View):
    def get(self, request):
        return render(request, 'energa.html')
