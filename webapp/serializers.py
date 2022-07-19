from rest_framework import serializers
from .models import clients

class clientsSerializers(serializers.ModelSerializer):
    class Meta:
        model =clients
        field = '__all__'


def clientsSerializer():
    