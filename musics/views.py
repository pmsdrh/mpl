from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import PlayListSerilizer
from .models import PlayList
from rest_framework.response import Response as R

# Create your views here.


class PlayListViewSet(viewsets.ViewSet):
    def list(self, request):
        srz_data = PlayListSerilizer(instance=PlayList.objects.all(), many=True)
        return R(data=srz_data.data)

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    
