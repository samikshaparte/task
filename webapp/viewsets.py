from rest_framework import viewsets
from . import models
from . import serializers


class clientsViewset(viewsets.ModelViewSet):
    queryset = models.clients.objects.all()
    serializer_class = serializers.clientsSerializer
