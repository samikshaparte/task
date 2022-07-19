from webapp.viewsets import clientsViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clients',clientsViewset)

# Localhost:p/api/clients/5
# GET, POST, UPDATE, DELETE
#  list , retrive
