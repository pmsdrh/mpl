from rest_framework import serializers
from .models import PlayList


class PlayListSerilizer(serializers.ModelSerilizer):
class Meta:
        model = PlayList
        fields = '__all__'
