from rest_framework import serializers
from .models import Hobbit

class HobbitSerializer(serializers.ModelSerializer):

    # def validate(self, data):

    #     if data:
    #         serializers

    class Meta:
        model = Hobbit
        fields = [
            'id',
            'name'
        ]