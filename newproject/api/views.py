# Response object will take in any python data or any serialized data we pass into it and will render a json data
from rest_framework.response import Response

# Since here we will use the function based apis so import api_view; we will use everywhere this in all our apis
from rest_framework.decorators import api_view

from base.models import Item
from .serializers import ItemSerializer

@api_view(['GET'])
def getData(request):
    # person = {'name':'Max', 'age': 25}
    items = Item.objects.all()  # Querying all items from the database
    serializer = ItemSerializer(items, many=True)  # many=True bcoz we want to serialize multiple items
    
    # return Response(person)  # Once the python dict is passed into the Response object it will return the json data
    return Response(serializer.data)  

@api_view(['POST'])
def addItem(request):
    # creating an object of the Serializer class
    serializer = ItemSerializer(data=request.data)
    
    # Validate it before saving into the db
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)




