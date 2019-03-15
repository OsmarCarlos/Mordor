from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from .models import Hobbit
from .serializers import HobbitSerializer
# Create your views here.

# Fuction base on view
# Class base on view

@api_view(['GET'])
def kingdom_places(request):
    places = ['Mordor', 'Rohan', 'Comarca', 'Gondor', 'Moria', 'Riverndell', 'Isuldur']
    response = [{'id': i, 'place': x} for i, x in enumerate(places)]
    return Response(response)


class HobbitViewSet(viewsets.ModelViewSet):

    queryset = Hobbit.objects.all()
    serializer_class = HobbitSerializer

    def list(self, request):
        queryset = self.get_queryset()
        print (queryset)
        serializer_class = self.get_serializer_class()

        serializer = serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        hobbit = self.get_object()
        serializer_class = self.get_serializer_class()

        serializer = serializer_class(hobbit)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(sefl, request, pk=None):
        pass

    @detail_route()
    def rings(self, request, pk=None):
        hobbit = self.get_object()
        return Response({
            'rings': hobbit.ring
        }, status=200)

