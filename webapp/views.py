from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import clientsSerializers
from clients.models import clients

class clientsAPIView(APIView):
    serializer_class = clientsSerializers

    def get_queryset(self):
        client = clients.objects.all()
        return clients
    def get(self, request, *args, **kwargs):
        clients = self.get_queryset()
        serializer = clientsSerializers(clients many=True)

        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        clients_data = request.data
         new_clients = clients.objects.create(clients_name=clients_data["client_name"], clients_id=clients_data[
             "client_id"], created_by=clients_data["created_by"], created_at=clients_data["created_at"])
         new_clients.save()

         serializer = clientsSerializers(new_clients)

         return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        clients_object = clients.objects.get()

        data = request.data

        clients_object.clients_name = data["client_name"]
        clients_object.clients_id = data["client_id"]
        clients_object.clients_createdby = data["client_createdby"]
        clients_object.clients_createdat = data["client_createdat"]

        clients_object.save()
        serializer = clientsSerializers(clients_object)
        return Response(serializer.data)

    def patch (self, request, *args, **kwargs):
        clients_object = clients.objects.get()
        data = request.data

        clients_object.clients_name = data.get("client_name", clients_object.clients_name)
        clients_object.clients_name = data.get("client_id", clients_object.clients_id)
        clients_object.clients_name = data.get("client_createdby", clients_object.clients_createdby)
        clients_object.clients_name = data.get("client_createdat", clients_object.clients_createdat)

        clients_object.save()
        serializer = clientsSerializer(clients_object)

        return  Response(serializer.data)
    def create(self, request, *args, **kwargs):
        clients_data = request.data
        new_client = clientsSpecs.objects.create(clients_name=clients_data["client_name"], client_model=clients_data["client_model"
            ], client_id=clients_data["client_id"], clients_createdby=clients_data["client_createdby"],client_createdat["client_createdat"])

        new_client.save()
        serializer = clientsSpecsSerializer(new_client)

        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        logedin_user = request.user
        if(logedin_user == "admin"):
            client = self.get_object()
            client.delete()
            response_message={"message":"Items has been deleted"}
        else:
            response_message={"message":"Not Allowed"}
        return Response(response_message)
