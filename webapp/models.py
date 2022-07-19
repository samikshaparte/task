from django.db import models

class clients(models.Model):
    clientid =models.IntegerField()
    clientname=models.CharField(max_length=10)
    createdby=models.CharField(max_length=10)
    createdat=models.DateTimeField()

    def __str__(self):
        return self.clientname
    #create / Insert /Add - POST
    # Retrieve / Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE


